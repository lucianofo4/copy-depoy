# Generated by Django 3.0 on 2022-06-29 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoursCalc', '0008_auto_20190110_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shift',
            name='break_time',
        ),
    ]
