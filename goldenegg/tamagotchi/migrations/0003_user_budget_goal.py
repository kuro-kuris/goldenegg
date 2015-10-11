# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamagotchi', '0002_auto_20151011_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='budget_goal',
            field=models.IntegerField(default=0),
        ),
    ]
