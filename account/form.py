from django.forms import forms

from account.models import Mail


class MailForm(forms.ModelForm):
    class Meta:
        modal = Mail
        fields = '__all__'

