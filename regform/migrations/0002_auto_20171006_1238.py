# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spiritualdata',
            name='are_you_a_baptized_catholic',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, verbose_name='Are you a babtized catholic ?'),
        ),
    ]
