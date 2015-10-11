# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamagotchi', '0003_user_budget_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
