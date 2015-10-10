# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('pet_name', models.CharField(max_length=200)),
                ('pet_health', models.IntegerField(default=100)),
                ('virtual_gold', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=0)),
                ('experience', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=200)),
                ('balance', models.IntegerField(default=0)),
                ('budget', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='user',
            field=models.ForeignKey(to='tamagotchi.User'),
        ),
    ]
