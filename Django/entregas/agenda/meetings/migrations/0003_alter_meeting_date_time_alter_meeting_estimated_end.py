# Generated by Django 5.0.2 on 2024-03-08 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_alter_meeting_date_time_alter_meeting_estimated_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='estimated_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
