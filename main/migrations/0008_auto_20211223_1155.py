# Generated by Django 3.1.6 on 2021-12-23 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20211204_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='notes',
            field=models.TextField(),
        ),
    ]
