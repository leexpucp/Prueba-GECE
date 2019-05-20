# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-20 00:09
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('prisoner_sr', '0004_auto_20190408_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='betray_payoff',
            field=otree.db.models.FloatField(default=20, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='betrayed_payoff',
            field=otree.db.models.FloatField(default=2, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='both_cooperate_payoff',
            field=otree.db.models.FloatField(default=12, null=True),
        ),
    ]