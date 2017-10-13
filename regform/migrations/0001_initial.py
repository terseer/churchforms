# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 10:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BioData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=60)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('marital_status', models.CharField(blank=True, choices=[('S', 'Single'), ('M', 'Married'), ('W', 'Widow'), ('W', 'Widower'), ('Se', 'Separated')], max_length=2)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('town', models.CharField(blank=True, max_length=100)),
                ('lga', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('residence', models.CharField(blank=True, max_length=300)),
                ('name_of_next_of_kin', models.CharField(blank=True, max_length=100)),
                ('address_of_next_of_kin', models.CharField(blank=True, max_length=200)),
                ('relation_with_next_of_kin', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChurchWorkHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catechetical_work', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('a', 'Teaching Catechisms'), ('b', 'Teaching in sunday school'), ('c', 'Teaching in marriage course'), ('d', 'Infant Baptism class')], max_length=5)),
                ('liturgical_work', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('a', 'Choir'), ('b', 'Proclamation(Layreader/Lector)'), ('c', 'Church wardens'), ('d', 'Alter Service')], max_length=5)),
                ('security_work', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('a', 'MOD'), ('b', 'Boys Brigade'), ('c', 'Security committee'), ('d', 'Not apply')], max_length=5)),
                ('environmental_work', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('a', 'Personal church cleaning'), ('b', 'Gardenning'), ('c', 'Societal church cleaning'), ('d', 'Not apply')], max_length=5)),
                ('health_work', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('a', 'Health committee'), ('b', 'Medical practitioner'), ('c', 'Midwifing'), ('d', 'Other, please specify')], max_length=4)),
                ('sports', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('a', 'Sports committee'), ('b', 'Trainer/Coach'), ('c', 'Umpire'), ('d', 'Sport team')], max_length=5)),
                ('other_work', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('a', 'Harvest and Bazaar'), ('b', 'Fund raising'), ('c', 'Building/Project'), ('d', 'Enlightenment and Awareness'), ('e', 'Finance'), ('f', 'Other, please specify')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(blank=True, max_length=100)),
                ('business_address', models.CharField(blank=True, max_length=200)),
                ('skills', models.CharField(blank=True, max_length=100)),
                ('sports', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SpiritualData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('are_you_a_baptized_catholic', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('not_baptized', models.CharField(blank=True, max_length=300)),
                ('are_you_a_communicant', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('not_communicant', models.CharField(blank=True, max_length=300)),
                ('are_you_confirmed', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('not_confirmed', models.CharField(blank=True, max_length=300)),
                ('are_wedded_in_the_church', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('not_wedded', models.CharField(blank=True, max_length=300)),
                ('any_tribal_community', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('not_in_tribal_community', models.CharField(blank=True, max_length=300)),
                ('in_tribal_community', models.CharField(blank=True, max_length=300)),
                ('member_of_any_pius_society', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('not_in_pius_society', models.CharField(blank=True, max_length=300)),
                ('yes_In_pius_society', models.CharField(blank=True, max_length=300)),
                ('belongs_to_any_organ_in_church', models.CharField(blank=True, choices=[('W', 'CWO'), ('M', 'CMO'), ('C', 'CYON')], max_length=1)),
                ('dont_belong_to', models.CharField(blank=True, max_length=300)),
                ('yes_belong_to', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('bio_data', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='regform.BioData')),
                ('church_work_history', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='regform.ChurchWorkHistory')),
                ('specialization', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='regform.Specialization')),
                ('spiritual_data', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='regform.SpiritualData')),
            ],
        ),
    ]
