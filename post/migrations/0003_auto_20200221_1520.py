# Generated by Django 3.0.3 on 2020-02-21 15:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200221_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 21, 15, 20, 45, 751580, tzinfo=utc), verbose_name='fecha de creacion'),
        ),
    ]
