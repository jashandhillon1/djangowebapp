# Generated by Django 2.2.4 on 2020-04-25 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200424_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 14, 4, 20, 476402), verbose_name='date published'),
        ),
    ]
