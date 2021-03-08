from .models import PhoneBook
from django.forms import ModelForm, TextInput


class UserForm(ModelForm):
    class Meta:
        model = PhoneBook
        fields = ["name", "surname", "address", "url", "phone", "pic"]

        widgets = {
            "name": TextInput(attrs={
                "class": 'form-control',
                "placeholder": "Type your name"
            }),
            "surname": TextInput(attrs={
                "class": 'form-control',
                "placeholder": "Type your surname"
            }),
            "address": TextInput(attrs={
                "class": 'form-control',
                "placeholder": "Type your address",
            }),
            "phone": TextInput(attrs={
                "class": 'form-control',
                "placeholder": "Type your phone-number",
                "pattern": "[0-9]{6,15}"
            }),

            "url": TextInput(attrs={
                "class": 'form-control',
                "placeholder": "Your url"
            }),

        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['address'].required = False
        self.fields['url'].required = False
        self.fields['pic'].required = False
