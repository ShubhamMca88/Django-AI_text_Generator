# main/views.py
from django.shortcuts import render
from django.http import JsonResponse
import openai

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def generate_text(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=100
        )
        return JsonResponse({'text': response.choices[0].text})
