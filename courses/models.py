# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from random import randrange, random, randint, choice
from datetime import timedelta, datetime
from djmoney.models.fields import MoneyField

# Create your models here.
class courses(models.Model):

	# This function will return a random datetime between two datetime objects.
	# @Param 	datetime, datetime 	(date range start, end)
	# @Return 	datetime 	(random date in the range)
	def random_date(start, end):
	    delta = end - start
	    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
	    random_second = randrange(int_delta)
	    return start + timedelta(seconds=random_second)

	# Python fiddle, called sing_sen_maker() by them
	# Makes a random senctence from the different parts of speech. Uses a SINGULAR subject
	# Used to build course descriptions
	# @Param	void
	# @Return 	string
	def randSentenceGen():
		s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman"]
		p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]
		s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "encourages", "meows on", "flees from", "tries to automate", "explodes"]
		p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "encourages", "meow on", "flee from", "try to automate", "explode"]
		infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology."]
		string = ""
		for i in range(5):
			# Map could be fun here
			# Explicit for readability
			string += choice(s_nouns) + " "
			string += choice(s_verbs) + " "
			string += choice(s_nouns).lower() + " " or choice(p_nouns).lower() + " "
			string += choice(infinitives) + "  "
		return string

	semester_start = datetime(2017, 5, 1, 18, 55, 35)
	semester_end = datetime(2017, 10, 1, 18, 55, 35)

	# FIELDS
	name = models.CharField(max_length=120)
	datetimes = models.DateTimeField(default = random_date(semester_start, semester_end))
	professors = models.CharField(max_length=120)
	cost = MoneyField(max_digits=4, decimal_places=0, default=randint(50,9000), default_currency='USD')
	description = models.TextField(default = randSentenceGen())

	# NOT USED
	# Replaced by django-money
	# @property
	# def cost(self):
	# 	return '$%s' %self.cost

	def __unicode__(self):
		return self.name


