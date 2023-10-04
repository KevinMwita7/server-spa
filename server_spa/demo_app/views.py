from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "demo_app/index.html")

def pricing(request):
    return render(request, "demo_app/pricing.html")

def faq(request):
    return render(request, "demo_app/faq.html")

def privacy(request):
    return render(request, "demo_app/privacy.html")

def about(request):
    return render(request, "demo_app/about.html")