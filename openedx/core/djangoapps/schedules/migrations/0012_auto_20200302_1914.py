# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-02 19:14


import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0011_auto_20200228_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='enrollment',
            field=models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='student.CourseEnrollment'),
        ),
    ]
