from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="demo_app_index"),
    path("pricing", views.pricing, name="demo_app_pricing"),
    path("faq", views.faq, name="demo_app_faq"),
    path("privacy", views.privacy, name="demo_app_privacy"),
    path("about", views.about, name="demo_app_about")
]