from django import forms
from .models import Contact

# creating a form
class ContactForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Contact
        # specify fields to be used
        fields = [
            "email",
            "subject",
            "message",
        ]