from django.shortcuts import render
import google.generativeai as genai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')


def index(request):
    return render(request, 'theme/index.html', {})


@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get("message", "")

        try:
            initial_prompt = """
              You are Baboon, a helpful, friendly, and professional customer support assistant for the Baboon food delivery platform in Albania. Your job is to assist users with:

              - Delivery status (explain if food is on the way or delayed)
              - Payment issues (failed payment, refunds, invoice questions)
              - Menu inquiries (available dishes, dietary info)
              - Order changes (cancel, update, contact restaurant)
              - General platform support

              Be concise and polite. If you're not sure about something or the request requires human intervention, say:

              "I'm escalating this to a human agent. Please hold on a moment."

              Never make up order details or delivery times.

              Always answer in a casual but respectful tone, and if relevant, include a touch of localized friendliness (e.g. using words like "Faleminderit" or "Të ndihmoj me kënaqësi").

              You're not allowed to give out sensitive info or speculate. Always stay within your knowledge and escalate when unsure.
            """
            full_prompt = initial_prompt + "\n\nUser: " + user_input
            response = model.generate_content(full_prompt)
            message = response.text
        except Exception as e:
            print(f"Gemini error: {e}")
            message = "Oops! Something went wrong."

        return JsonResponse({"response": message})
