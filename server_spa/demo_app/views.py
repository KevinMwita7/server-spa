from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ContactUsForm

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

def contact_us(request):
    if (request.method == "POST"):
        form = ContactUsForm(request.POST)
        if (form.is_valid()):
            response = redirect("/success")
            response.status_code = 303
            return response
    else:
        form = ContactUsForm()

    return render(request, "demo_app/contact_us.html", { "template": _base_template(request), "form": form })

def success(request):
    # This page can only be accessed on successful form submissions
    if "X-Requested-With" not in request.headers or request.headers["X-Requested-With"] != "XMLHttpRequest": 
        return HttpResponseRedirect("/")
    return render(request, "demo_app/success.html", { "template": _base_template(request) })
    

# Python has no private access modifiers. To work around this, one adds an underscore (_) before the function
# or variable to signal to other devs that they are meant to be private. Note that they can still be accessed
# outside the module since Python does not enforce the convention. It simply trusts that everyone is a "consenting adult"
def _base_template(request):
    return "demo_app/base_empty.html" if "X-Requested-With" in request.headers and request.headers["X-Requested-With"] == "XMLHttpRequest" else "demo_app/base.html"