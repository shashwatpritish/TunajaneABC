# Importing django and textblob

from django.shortcuts import render, HttpResponse
from .models import Text, Contact
from textblob import TextBlob

# My views here.
def home(request):
    if request.method == "POST":
        word = request.POST.get('word')
        text = Text(word=word)
        text.save()
        words =TextBlob(word)
        myword = words.correct()
        texts = {
            "text": myword
        }
        return render(request,'index.html',texts)
    return render(request,'index.html')

def use(request):
    return render(request,'use.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data = Contact(name=name,email=email,message=message)
        data.save()
    return render(request,'contact.html')