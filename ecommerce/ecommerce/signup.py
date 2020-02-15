from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from django.conf import settings



class Signupform(forms.Form):
    yourname = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(required=False,label='Your e-mail address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

def signup(request):
    submitted = False
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email'),
                ['yotake@luc.edu'],
                connection=con
            )
            return HttpResponseRedirect('/signup?submitted=True')
    else:
        form = Signupform()
        if 'submitted' in request.GET:
            submitted = True
 
    return render(request, 'signup/signup.html', {'form': form, 'submitted': submitted})
