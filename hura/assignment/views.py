from django.contrib.auth import authenticate, login
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext

from assignment.models import Professor


class LoginForm(forms.Form):
    username = forms.CharField(label=(u'username'))
    password = forms.CharField(label=(u'password'), widget=forms.PasswordInput(render_value=False))

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if Professor.objects.filter(user=user).exists():
                    return HttpResponseRedirect('/prof_welcome')
                else:
                    return HttpResponseRedirect('/stud_welcome')
            else:
                errors = form._errors.setdefault("no_field", form.error_class())
                errors.append("validation Error")
                return render_to_response('login.html', {'form': form},
                                          context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
    else:
        '''user is not submitting the form, show the login form'''
        form = LoginForm()
        context = {'form': form}
        return render_to_response('login.html', context, context_instance=RequestContext(request))


def StudWelcome(request):
    if request.user.is_authenticated():

    else :
        HttpResponseRedirect('insti/login/')