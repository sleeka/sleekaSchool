# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from sleekaSchool.models import courses
from datetime import datetime
from moneyed import Money, USD

# Create your tests here.
# @TODO
class CoursesTestCase(TestCase):
	currentDatetime = datetime.now()
	def createCourse(self):
		courses.objects.create(
			name='Algebra-4001-B',
			datetimes=currentDatetime,
			professors='Bob Barker',cost=Money(500, USD),
			description='Algebra is the study of mathematical symbols and\
			 the rules for manipulating these symbols'
			)
		courses.objects.create(
			name='Accounting-1022-A',
			datetimes=currentDatetime,
			professors='Homer Simpson',cost=Money(1000, USD),
			description='Accounting measures the results of an organization\
			\'s economic activities and conveys this information to a variet\
			y of users'
			)
		courses.objects.create(
			name='ComputerScience-4021-C',
			datetimes=currentDatetime,
			professors='Bob Dole',cost=Money(1500, USD),
			description='Computer science is the study of the theory, \
			experimentation, and engineering that form the basis for the\
			 design and use of computers.'
			)
		courses.objects.create(
			name='Engineering-1234-D',
			datetimes=currentDatetime,
			professors='William Cannon',cost=Money(2000, USD),
			description='Engineering is the application of mathematics and\
			 scientific, economic, social, and practical knowledge in order\
			  to invent, innovate, design, build, maintain, research, and\
			   improve structures, machines, tools, systems, components,\
			    materials, processes, solutions, and organizations.'
			)

	def testNames(self):
		algebra = courses.objects.get(name='Algebra-4001-B')
		accounting = courses.objects.get(name='Accounting-1022-A')
		computerScience = courses.objects.get(name='ComputerScience-4021-C')
		engineering = courses.objects.get(name='Engineering-1234-D')
		# self.assertEqual(algebra, ...)
		# self.assertEqual(accounting, ...)
		# self.assertEqual(computerScience, ...)
		# self.assertEqual(engineering, ...)
	def testDatetimes(self):
		allFour = courses.objects.get(datetimes=currentDatetime)
		self.assertEqual(len(allFour), 4)

	def testProfessorNames(self):
		algebra = courses.objects.get(professors='')
		accounting = courses.objects.get(professors='')
		computerScience = courses.objects.get(professors='')
		engineering = courses.objects.get(professors='')
	def testCost(self):
		algebra = courses.objects.get(cost=Money(500, USD))
		accounting = courses.objects.get(cost=Money(1000, USD))
		computerScience = courses.objects.get(cost=Money(1500, USD))
		engineering = courses.objects.get(cost=Money(2000, USD))
		# self.assertEquals(...)
	def testDescription(self):
		algebra = courses.objects.get(description='')
		accounting = courses.objects.get(nadescriptionme='')
		computerScience = courses.objects.get(description='')
		engineering = courses.objects.get(description='')

