# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
	context = locals()
	template = 'home.html'
	return render(request, template, context)

def enroll(request):
	context = locals()
	template = 'enroll.html'
	return render(request, template, context)

def mySchedule(request):
	context = locals()
	template = 'mySchedule.html'
	return render(request, template, context)

def clearSchedule(request):
	context = locals()
	template = 'mySchedule.html'
	return render(request, template, context)

def optimizeSchedule(request):
	context = locals()
	template = 'mySchedule.html'
	return render(request, template, context)

def registerAll(request):
	context = locals()
	template = 'mySchedule.html'
	return render(request, template, context)