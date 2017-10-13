# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regform', '0002_auto_20171006_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='address_of_next_of_kin',
            field=models.CharField(blank=True, max_length=200, verbose_name='Address of next kin:'),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='email',
            field=models.EmailField(blank=True, max_length=200, verbose_name='Enter valid Email Address: (example abc@example.com)'),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='lga',
            field=models.CharField(blank=True, max_length=100, verbose_name='L. G. A.'),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('S', 'Single'), ('M', 'Married'), ('W', 'Widow'), ('W', 'Widower'), ('Se', 'Separated')], max_length=2, verbose_name='Marital Status:'),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='name_of_next_of_kin',
            field=models.CharField(blank=True, max_length=100, verbose_name='Name of next of Kin:'),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='phone',
            field=models.CharField(blank=True, max_length=100, verbose_name='Phone:'),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='relation_with_next_of_kin',
            field=models.CharField(blank=True, max_length=100, verbose_name='Relationship with next of kin:'),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='residence',
            field=models.CharField(blank=True, max_length=300, verbose_name='Home Address:'),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='state',
            field=models.CharField(blank=True, max_length=100, verbose_name='State of Origin:'),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='town',
            field=models.CharField(blank=True, max_length=100, verbose_name='Town:'),
        ),
        migrations.AlterField(
            model_name='spiritualdata',
            name='any_tribal_community',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, verbose_name='Do you belong to any tribal communities in the church ? '),
        ),
        migrations.AlterField(
            model_name='spiritualdata',
            name='are_wedded_in_the_church',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, verbose_name='Are you wedded in the church ? '),
        ),
        migrations.AlterField(
            model_name='spiritualdata',
            name='are_you_a_communicant',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, verbose_name='Are you a communicant ? '),
        ),
        migrations.AlterField(
            model_name='spiritualdata',
            name='are_you_confirmed',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, verbose_name='Are you confirmed ? '),
        ),
        migrations.AlterField(
            model_name='spiritualdata',
            name='belongs_to_any_organ_in_church',
            field=models.CharField(blank=True, choices=[('W', 'CWO'), ('M', 'CMO'), ('C', 'CYON')], max_length=1, verbose_name='Do you belong to any of the three organs in the church ?'),
        ),
        migrations.AlterField(
            model_name='spiritualdata',
            name='dont_belong_to',
            field=models.CharField(blank=True, max_length=300, verbose_name='If no, please state reasons:'),
        ),
        migrations.AlterField(
            model_name='spiritualdata',
            name='in_tribal_community',
            field=models.CharField(blank=True, max_length=300, verbose_name='If yes, please, state the community:'),
        ),
        migrations.AlterField(
            model_name='spiritualdata',
            name='member_of_any_pius_society',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, verbose_name='Are you a member of any pius societies in the church ? '),
        ),
        migrations.AlterField(
            model_name='spiritualdata',
            name='not_baptized',
            field=models.CharField(blank=True, max_length=300, verbose_name='If no, please, state your reasons:'),
        ),
        migrations.AlterField(
            model_name='spiritualdata',
            name='not_communicant',
            field=models.CharField(blank=True, max_length=300, verbose_name='If no, please, state your reasons'),
        ),
        migrations.AlterField(
            model_name='spiritualdata',
            name='not_confirmed',
            field=models.CharField(blank=True, max_length=300, verbose_name='If no, please, state your reasons:'),
        ),
        migrations.AlterField(
            model_name='spiritualdata',
            name='not_in_pius_society',
            field=models.CharField(blank=True, max_length=300, verbose_name='If no, please state your reasons:'),
        ),
        migrations.AlterField(
            model_name='spiritualdata',
            name='not_in_tribal_community',
            field=models.CharField(blank=True, max_length=300, verbose_name='If no, please, state reasons:'),
        ),
        migrations.AlterField(
            model_name='spiritualdata',
            name='not_wedded',
            field=models.CharField(blank=True, max_length=300, verbose_name='If no, please, state your reasons:'),
        ),
        migrations.AlterField(
            model_name='spiritualdata',
            name='yes_In_pius_society',
            field=models.CharField(blank=True, max_length=300, verbose_name='If yes, please, state the society:'),
        ),
        migrations.AlterField(
            model_name='spiritualdata',
            name='yes_belong_to',
            field=models.CharField(blank=True, max_length=300, verbose_name='If yes, please, state the organ:'),
        ),
    ]
