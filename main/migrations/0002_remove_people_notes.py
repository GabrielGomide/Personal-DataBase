# Generated by Django 3.1.6 on 2021-11-01 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='notes',
        ),
    ]
