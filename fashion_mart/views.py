from django.shortcuts import render

def home(request):
    return render(request, 'fashion_mart/home.html')
