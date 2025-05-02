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
            response = model.generate_content(user_input)
            message = response.text
        except Exception as e:
            print(f"Gemini error: {e}")
            message = "Oops! Something went wrong."

        return JsonResponse({"response": message})
