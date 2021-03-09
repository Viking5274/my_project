from django import forms

from .models import PhoneBook
from django.forms import ModelForm, TextInput


class UserForm(ModelForm):
    class Meta:
        model = PhoneBook
        fields = ["name", "surname", "address_country", "address_city", "address_street", "url", "phone", "pic"]

        widgets = {
            "name": TextInput(attrs={
                "class": 'form-control',
                "placeholder": "Type your name"
            }),
            "surname": TextInput(attrs={
                "class": 'form-control',
                "placeholder": "Type your surname"
            }),
            "address_country": TextInput(attrs={
                "class": 'form-control',
                "placeholder": "Type your address",
            }),
            "address_city": TextInput(attrs={
                "class": 'form-control',
                "placeholder": "Type your address",
            }),
            "address_street": TextInput(attrs={
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

        self.fields['address_country'].required = False
        self.fields['address_city'].required = False
        self.fields['address_street'].required = False
        self.fields['url'].required = False
        self.fields['pic'].required = False

    def clean(self):
        print(self)
        address_country = self.cleaned_data.get('address_country')
        address_city = self.cleaned_data.get('address_city')
        address_street = self.cleaned_data.get('address_street')
        name = self.cleaned_data.get('name')
        surname = self.cleaned_data.get('surname')
        phone = self.cleaned_data.get('phone')
        for i in PhoneBook.objects.all():
            if (name == i.name and surname == i.surname) and id != i.id:
                raise forms.ValidationError({'surname': u'Error: User with this name and surname is already exist'})
            if i.phone == phone:
                raise forms.ValidationError({'phone': u'Error: This phone is already exits'})
            if address_street != '' or address_city != '' or address_country != '':
                if not (address_street != '' and address_city != '' and address_country != ''):
                    raise forms.ValidationError(
                        {'address_city': u'Error: If you want fill address, please fill all fields'})
        return self.cleaned_data


class EditForm(ModelForm):
    class Meta:
        model = PhoneBook
        fields = ["name", "surname", "address_country", "address_city", "address_street", "url", "phone", "pic"]

        widgets = {
            "name": TextInput(attrs={
                "class": 'form-control',
                "placeholder": "Type your name"
            }),
            "surname": TextInput(attrs={
                "class": 'form-control',
                "placeholder": "Type your surname"
            }),
            "address_country": TextInput(attrs={
                "class": 'form-control',
                "placeholder": "Type your address",
            }),
            "address_city": TextInput(attrs={
                "class": 'form-control',
                "placeholder": "Type your address",
            }),
            "address_street": TextInput(attrs={
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
        super(EditForm, self).__init__(*args, **kwargs)

        self.fields['address_country'].required = False
        self.fields['address_city'].required = False
        self.fields['address_street'].required = False
        self.fields['url'].required = False
        self.fields['pic'].required = False
