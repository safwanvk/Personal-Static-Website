from django.urls import path
from django.views.generic import TemplateView

from account import views

urlpatterns = [

    path('', views.contact, name='contact'),

]