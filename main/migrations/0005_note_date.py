# Generated by Django 3.1.6 on 2021-11-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
