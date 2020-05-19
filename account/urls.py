from django.urls import path
from django.views.generic import TemplateView

from account import views

urlpatterns = [

    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('send-form-email', views.SendFormEmail.as_view(), name='send_email')
]