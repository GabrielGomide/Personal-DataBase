# Generated by Django 3.1.6 on 2021-11-01 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_people_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='notes',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
