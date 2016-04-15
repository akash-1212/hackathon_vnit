import datetime
import random
from datetime import date

from django import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404, redirect

from .forms import PostForm

# Create your views here.
from django.template import RequestContext

from assignment.models import Stud_course
from .models import Professor, Assignment, Prof_course, Course, Student, stud_subm


class LoginForm(forms.Form):
    username = forms.CharField(label=(u'username'))
    password = forms.CharField(label=(u'password'), widget=forms.PasswordInput(render_value=False))


def randomword():
    choose = "qwertyuiopasdfghjklzxcvbnm1234567890AQWSEDRFTGYHUJIKOLPZXCVBNM"
    return ''.join(random.choice(choose) for i in range(10))


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
            return render_to_response('user_mismatch.html', {'message': "User mismatch"},
                                      context_instance=RequestContext(request))
    else:
        HttpResponseRedirect('insti/login/')


def ProfWelcome(request):
    if request.user.is_authenticated():
        if Professor.objects.filter(user=request.user).exists():
            my_assignments_present = Assignment.objects.filter(prof=request.user,
                                                               deadline__gte=datetime.datetime.today()).order_by(
                'deadline')
            my_assignments_past = Assignment.objects.filter(prof=request.user,
                                                            deadline__lt=datetime.datetime.today()).order_by('deadline')
        else:
            render_to_response('user_mismatch.html', {'message': "User mismatch"},
                               context_instance=RequestContext(request))
    else:
        HttpResponseRedirect('login/')


def Prof_assign_details(request, key):
    if request.user.is_authenticated():
        if Professor.objects.filter(user=request.user).exists():
            assignment = get_object_or_404(Assignment, key=key)
            return render(request, 'a_details.html', {'details': assignment})
        else:
            render_to_response('user_mismatch.html', {'message': "User mismatch"},
                               context_instance=RequestContext(request))
    else:
        HttpResponseRedirect('login/')


def new_assign(request):
    if request.user.is_authenticated():
        prof = Professor.objects.filter(user=request.user)
        if prof.exists():
            prof = prof[0]
            if request.method == "POST":
                form = PostForm(request.POST)
                if form.is_valid():
                    assign = form.save(commit=False)
                    course = Course.objects.filter(course_name=request.POST.get('course'))[0]
                    prof_course = Prof_course.objects.filter(course=course, prof=prof)
                    assign.id = randomword()
                    assign.prof_course = prof_course
                    assign.save()
                    return redirect('details', key=assign.key)
            else:
                form = PostForm()
            return render(request, 'post_edit.html', {'form': form})
        else:
            render_to_response('user_mismatch.html', {'message': "User mismatch"},
                               context_instance=RequestContext(request))
    else:
        HttpResponseRedirect('login/')


def Prof_assign_edit_details(request, key):
    if request.user.is_authenticated():
        prof = Professor.objects.filter(user=request.user)
        if prof.exists():
            prof = prof[0]
            assign = get_object_or_404(Assignment, key=key)
            if request.method == "POST":
                form = PostForm(request.POST, instance=assign)
                if form.is_valid():
                    assign = form.save(commit=False)
                    course = Course.objects.filter(course_name=request.POST.get('course'))[0]
                    prof_course = Prof_course.objects.filter(course=course, prof=prof)
                    assign.id = randomword()
                    assign.modified = True
                    assign.modified_date = datetime.datetime.now()
                    assign.prof_course = prof_course
                    assign.save()
                    return redirect('details', key=assign.key)
            else:
                form = PostForm(instance=assign)
            return render(request, 'post_edit.html', {'form': form})
        else:
            render_to_response('user_mismatch.html', {'message': "User mismatch"},
                               context_instance=RequestContext(request))
    else:
        HttpResponseRedirect('login/')


def Prof_submitted_assignment(request):
    if request.user.is_authenticated():
        if Professor.objects.filter(user=request.user).exists():
            aid = request.POST.get('id')
            submitted = stud_subm.objects.filter(assignment=aid)
        else:
            render_to_response('user_mismatch.html', {'message': "User mismatch"},
                               context_instance=RequestContext(request))
    else:
        HttpResponseRedirect('login/')


def Stud_view_submitted(request):
    if request.user.is_authenticated():
        if Student.objects.filter(user=request.user).exists():
            assign = stud_subm.objects.filter(stud=request.user)
        else:
            render_to_response('user_mismatch.html', {'message': "User mismatch"},
                               context_instance=RequestContext(request))
    else:
        HttpResponseRedirect('login/')

