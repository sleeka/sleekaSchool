# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 19:55
from __future__ import unicode_literals

import datetime
from decimal import Decimal
from django.db import migrations, models
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20170505_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='cost',
            field=djmoney.models.fields.MoneyField(decimal_places=0, default=Decimal('3916'), default_currency=b'USD', max_digits=4),
        ),
        migrations.AlterField(
            model_name='courses',
            name='datetimes',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 22, 7, 52, 46)),
        ),
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=models.TextField(default='Some guy kicks this cool guy my gardener met yesterday for no apparent reason.  Some guy eats a sloth for a disease.  A dude eats a dude for a disease.  A cat with rabies eats a sloth because the sky is green.  Superman configures a dude for no apparent reason.  '),
        ),
    ]
