# Generated by Django 4.1.1 on 2022-09-20 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("messagex", "0005_messagex_etext_messagex_subject_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="messagex",
            old_name="timestamp",
            new_name="time_stamp",
        ),
        migrations.AlterField(
            model_name="messagex",
            name="subject",
            field=models.CharField(
                default="", max_length=256, verbose_name="Message Subject"
            ),
        ),
    ]
