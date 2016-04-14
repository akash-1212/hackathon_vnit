from __future__ import unicode_literals
from django.contrib.auth.admin import User
from django.db import models

class Student(models.Model):
    user=models.OneToOneField(User)
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=3)
    email=models.EmailField()
    section=models.CharField(max_length=1)
    # courses=models.CharField(max_length=60)

class Professor(models.Model):
    user=models.OneToOneField(User)
    name=models.CharField(max_length=50,primary_key=True)
    # courses=models.CharField(max_length=50)
    email=models.EmailField()

class Course(models.Model):
    course_id=models.CharField(max_length=6,primary_key=True)
    course_name=models.CharField(max_length=40)

class Prof_course(models.Model):
    course=models.ForeignKey(Course)
    prof=models.ForeignKey(Professor)

class Stud_course(models.Model):
    course=models.ForeignKey(Course)
    stud=models.ForeignKey(Student)
    reg_time=models.DateField()


class Assignment(models.Model):
    id=models.CharField(max_length=10,primary_key=True)
    name=models.CharField(max_length=10)
    course=models.ForeignKey(Course)
    prof=models.ForeignKey(Professor)
    time_uploaded=models.DateField(auto_now=True)

class assign_section(models.Model):
    assign=models.ForeignKey(Assignment)
    deadline=models.DateField()
    section=models.CharField(max_length=1)

class stud_subm(models.Model):
    stud=models.ForeignKey(Student)
    assignment=models.ForeignKey(Assignment)
    subm_time=models.DateField()