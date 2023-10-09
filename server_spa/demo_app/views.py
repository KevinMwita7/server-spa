from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "demo_app/index.html", { "template": _base_template(request) })

def pricing(request):
    return render(request, "demo_app/pricing.html", { "template": _base_template(request) })

def faq(request):
    return render(request, "demo_app/faq.html", { "template": _base_template(request) })

def privacy(request):
    return render(request, "demo_app/privacy.html", { "template": _base_template(request) })

def about(request):
    return render(request, "demo_app/about.html", { "template": _base_template(request) })

# Python has no private access modifiers. To work around this, one adds an underscore (_) before the function
# or variable to signal to other devs that they are meant to be private. Note that they can still be accessed
# outside the module since Python does not enforce the convention. It simply trusts that everyone is a "consenting adult"
def _base_template(request):
    return "demo_app/base_empty.html" if "X-Requested-With" in request.headers and request.headers["X-Requested-With"] == "XMLHttpRequest" else "demo_app/base.html"