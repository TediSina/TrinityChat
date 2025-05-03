from django.shortcuts import render, redirect
import google.generativeai as genai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage, ChatSession
import uuid
import json


genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')


def index(request):
    return render(request, 'chat/index.html', {})


@csrf_exempt
def chatbot(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Invalid request method"}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    user_input = data.get("message")
    if not user_input:
        return JsonResponse({"error": "No message provided"}, status=400)

    session_id = data.get("session_id", str(uuid.uuid4()))
    order_history = data.get("order_history", "").strip()

    ChatMessage.objects.create(sender="user", message=user_input, session_id=session_id)

    session, _ = ChatSession.objects.get_or_create(session_id=session_id)

    if order_history:
        session.order_history = order_history
        session.save()
    else:
        order_history = session.order_history or ""

    if session.is_human:
        return

    try:
        initial_prompt = """
            You are Baboon, a helpful, friendly, and professional customer support assistant for the Baboon food delivery platform in Albania.

            Your job is to assist users with:
            - Delivery status (explain if food is on the way or delayed)
            - Payment issues (failed payment, refunds, invoice questions)
            - Menu inquiries (available dishes, dietary info)
            - Order changes (cancel, update, contact restaurant)
            - General platform support

            You MUST escalate to a human agent in the following cases:
            - The user says the food is very late or not delivered after the estimated time
            - You don't see the order they're talking about in the order history
            - The user is angry or repeatedly unsatisfied
            - The issue requires contacting a restaurant or processing a refund
            - You're unsure how to solve their problem

            When escalating, say:
            "I'm escalating this to a human agent. Please hold on a moment." in English or in Albanian based on the user's language.

            Rules:
            - Never invent order details or delivery times. Only use what's in the order history.
            - Use a respectful, casual tone in all replies.
            - Do not give out personal information.
            - Answer based only on the chat and order history below. If unsure, escalate.
        """

        if order_history:
            initial_prompt += f"\n\nHere is the user's order history:\n{order_history}\n"

        history = ChatMessage.objects.filter(session_id=session_id).order_by("-timestamp")[:5][::-1]
        chat_history = "\n\n".join(
            f"{'User' if msg.sender == 'user' else 'Bot'}: {msg.message}" for msg in history
        )

        full_prompt = f"{initial_prompt}\n\nChat History:\n{chat_history}\n\nUser: {user_input}"

        response = model.generate_content(full_prompt)
        ai_message = response.text.strip()

        lower_msg = ai_message.lower()
        keyword_trigger = any(phrase in lower_msg for phrase in [
            "not sure", "i don't know", "can't help", "escalate", "human agent",
            "contact support", "i'll pass you to", "do të kaloj te", "nuk jam i sigurt", "nuk mundem"
        ])

        if keyword_trigger:
            session.is_human = True
            session.save()
            ChatMessage.objects.create(sender="bot", message=ai_message, session_id=session_id)
            return JsonResponse({"response": ai_message, "escalated": True})

        ChatMessage.objects.create(sender="bot", message=ai_message, session_id=session_id)
        return JsonResponse({"response": ai_message, "escalated": False})

    except Exception as e:
        print(f"Gemini error: {e}")
        ChatMessage.objects.create(sender="bot", message="Oops! Something went wrong.", session_id=session_id)
        return JsonResponse({"response": "Oops! Something went wrong.", "escalated": False})


def operator_dashboard(request):
    sessions = ChatMessage.objects.values_list("session_id", flat=True).distinct()
    session_id = request.GET.get("session", sessions[0] if sessions else None)
    messages = ChatMessage.objects.filter(session_id=session_id).order_by("timestamp") if session_id else []

    is_human = False
    if session_id:
        chat_session = ChatSession.objects.filter(session_id=session_id).first()
        is_human = chat_session.is_human if chat_session else False

    if request.method == "POST":
        reply = request.POST.get("reply")
        session_id = request.GET.get("session")
        if session_id and reply:
            ChatMessage.objects.create(sender="human", message=reply, session_id=session_id)
            ChatSession.objects.update_or_create(session_id=session_id, defaults={"is_human": True})

    return render(request, "chat/dashboard.html", {
        "messages": messages,
        "sessions": sessions,
        "current": session_id,
        "is_human": is_human,
    })


@csrf_exempt
def get_chat_history(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            session_id = data.get("session_id")
            if not session_id:
                return JsonResponse({"error": "Missing session_id"}, status=400)

            messages = ChatMessage.objects.filter(session_id=session_id).order_by("timestamp")
            session = ChatSession.objects.filter(session_id=session_id).first()

            chat_data = [
                {"sender": msg.sender, "message": msg.message, "timestamp": msg.timestamp.isoformat()}
                for msg in messages
            ]
            return JsonResponse({
                "chat": chat_data,
                "order_history": session.order_history if session else ""
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST method allowed"}, status=405)


@csrf_exempt
def get_session_status(request):
    if request.method == "POST":
        data = json.loads(request.body)
        session_id = data.get("session_id")
        session = ChatSession.objects.filter(session_id=session_id).first()
        is_human = session.is_human if session else False
        return JsonResponse({"is_human": is_human})
