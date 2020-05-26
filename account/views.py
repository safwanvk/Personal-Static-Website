from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import View, FormView
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail

from account.forms import  ContactModelForm


def contact(request):
    form = ContactModelForm()
    # if request.method == 'POST':
    #     form = ContactModelForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('contact')
    if request.is_ajax():
        form = ContactModelForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'index.html', {'form': form})


