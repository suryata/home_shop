# Generated by Django 4.2.5 on 2023-09-19 05:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date_added',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
