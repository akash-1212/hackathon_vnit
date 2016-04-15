import json
from datetime import date

import simplejson as simplejson
from django import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

# Create your views here.
from django.template import RequestContext

from assignment.models import Professor, Student, Stud_course, Prof_course, Assignment, stud_subm


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
        stud = Student.objects.filter(user=request.user)
        if stud.exists():
            stud = stud[0]
            stud_reg_course_list = Stud_course.objects.filter(stud=stud).values_list('course', flat=True)
            prof_course = Prof_course.objects.filter(course__in=stud_reg_course_list)
            prof_course_list = Prof_course.objects.filter(course__in=stud_reg_course_list).values_list(
                'course__course_name', 'prof__name')
            # print(prof_course_list)
            prof_course_merged_list = {}
            for prof_course_ in prof_course_list:
                if not prof_course_[0] in prof_course_merged_list:
                    # prof_course_[0] =course
                    # prof_course_[1]= prof name
                    prof_course_merged_list[prof_course_[0]] = []
                prof_course_merged_list[prof_course_[0]].append(prof_course_[1])
            # TODO one required output
            print(prof_course)
            assign_list_submitable = Assignment.objects.filter(prof_course__in=prof_course, deadline__gte=date.today())
            assign_list_dead = Assignment.objects.filter(prof_course=prof_course, deadline__lt=date.today())

            submission_list = stud_subm.objects.filter(stud=stud).values_list('assignment', flat=True)
            # print(prof_course_merged_list)
            # for key, value in prof_course_merged_list.items():
            #     print ("key" + key)
            #     for item in value:
            #         print ("val" + item)
            # prof_course_merged_list_obj=json.dumps(prof_course_merged_list)
            # print(str(prof_course_merged_list_obj))
            # print(str(assign_list_submitable.query))
            return render_to_response('question_papers.html',
                               {'dead_assign': assign_list_dead, "live_assign": assign_list_submitable,
                                "prof_course_pair": prof_course_merged_list, 'submission_list': submission_list},
                               context_instance=RequestContext(request))
        else:
            # TODO add logout button in template
            return  render_to_response('user_mismatch.html', {'message': "User mismatch"},
                               context_instance=RequestContext(request))
    else:
        HttpResponseRedirect('insti/login/')
