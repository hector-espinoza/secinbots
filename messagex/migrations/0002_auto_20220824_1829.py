# Generated by Django 3.0.4 on 2022-08-24 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messagex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Message Timestamp'),
        ),
    ]
