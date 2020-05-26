from django import forms

from account.models import Contact


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'



