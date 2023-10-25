from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="demo_app_index"),
    path("pricing", views.pricing, name="demo_app_pricing"),
    path("faq", views.faq, name="demo_app_faq"),
    path("privacy", views.privacy, name="demo_app_privacy"),
    path("about", views.about, name="demo_app_about"),
    path("contact_us", views.contact_us, name="demo_app_contact_us"),
    path("success", views.success, name="demo_app_success")
]