from django.shortcuts import render
import google.generativeai as genai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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

    order_history = data.get("order_history", "").strip()
    chat_history = data.get("history", [])
    if not isinstance(chat_history, list):
        chat_history = []

    if data.get("is_human"):
        return JsonResponse({
            "response": "A human agent has joined this chat.",
            "escalated": True,
        })

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

        formatted_history = []
        for msg in chat_history[-8:]:
            sender = msg.get("sender", "user")
            label = {
                "user": "User",
                "bot": "Bot",
                "human": "Human agent",
            }.get(sender, sender.title())
            formatted_history.append(f"{label}: {msg.get('message', '')}")

        history_text = "\n\n".join(formatted_history)

        full_prompt = f"{initial_prompt}\n\nChat History:\n{history_text}\n\nLatest user message: {user_input}"

        response = model.generate_content(full_prompt)
        ai_message = response.text.strip()

        lower_msg = ai_message.lower()
        keyword_trigger = any(phrase in lower_msg for phrase in [
            "not sure", "i don't know", "can't help", "escalate", "human agent",
            "contact support", "i'll pass you to", "do të kaloj te", "nuk jam i sigurt", "nuk mundem"
        ])

        if keyword_trigger:
            return JsonResponse({"response": ai_message, "escalated": True})

        return JsonResponse({"response": ai_message, "escalated": False})

    except Exception as e:
        print(f"Gemini error: {e}")
        return JsonResponse({"response": "Oops! Something went wrong.", "escalated": False})


def operator_dashboard(request):
    return render(request, "chat/dashboard.html", {})


@csrf_exempt
def get_chat_history(request):
    if request.method == "POST":
        return JsonResponse({"chat": [], "order_history": ""})

    return JsonResponse({"error": "Only POST method allowed"}, status=405)


@csrf_exempt
def get_session_status(request):
    if request.method == "POST":
        return JsonResponse({"is_human": False})

    return JsonResponse({"error": "Only POST method allowed"}, status=405)
