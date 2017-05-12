# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 15:04
from __future__ import unicode_literals

import datetime
from decimal import Decimal
from django.db import migrations, models
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20170505_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='cost',
            field=djmoney.models.fields.MoneyField(decimal_places=0, default=Decimal('2121'), default_currency=b'USD', max_digits=4),
        ),
        migrations.AlterField(
            model_name='courses',
            name='datetimes',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 23, 22, 14, 44)),
        ),
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=models.TextField(default='The king configures a sloth for no apparent reason.  Superman flees from some guy to know more about archeology.  Your homie treats my mom to make a pie.  A cat with rabies gives this cool guy my gardener met yesterday for a disease.  Some guy spies on some guy for no apparent reason.  '),
        ),
    ]
