from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AddressForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def sendmail(request):
    if request.method=='POST':
        form=AddressForm(request.POST)
        if form.is_valid():
            send_email(form)
            return HttpResponseRedirect('success')
    else:
        form=AddressForm()
    return render(request, 'address.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def send_email(form):
    subject="Mail from drylab"
    message="Dear " + form.cleaned_data["name"] + "\n" + "You have been successfully registered"
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[form.cleaned_data['email']]
    send_mail(subject, message, email_from, recipient_list)
    pass
