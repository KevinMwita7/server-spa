from django import forms

# https://docs.djangoproject.com/en/4.2/topics/forms/#working-with-forms
class ContactUsForm(forms.Form):
    your_name = forms.CharField()
    your_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea())