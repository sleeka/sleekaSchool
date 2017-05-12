# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import courses

class coursesAdmin(admin.ModelAdmin):
	class Meta:
		model = courses

admin.site.register(courses, coursesAdmin)
