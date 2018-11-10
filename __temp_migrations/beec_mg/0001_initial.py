# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-08 21:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('total_contribution1', otree.db.models.CurrencyField(default=0, null=True)),
                ('total_contribution2', otree.db.models.CurrencyField(default=0, null=True)),
                ('total_contribution3', otree.db.models.CurrencyField(default=0, null=True)),
                ('mean_contribution1', otree.db.models.CurrencyField(default=0, null=True)),
                ('mean_contribution2', otree.db.models.CurrencyField(default=0, null=True)),
                ('mean_contribution3', otree.db.models.CurrencyField(default=0, null=True)),
                ('totalp1', otree.db.models.IntegerField(default=0, null=True)),
                ('totalp2', otree.db.models.IntegerField(default=0, null=True)),
                ('totalp3', otree.db.models.IntegerField(default=0, null=True)),
                ('individual_share1', otree.db.models.CurrencyField(default=0, null=True)),
                ('individual_share2', otree.db.models.CurrencyField(default=0, null=True)),
                ('individual_share3', otree.db.models.CurrencyField(default=0, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beec_mg_group', to='otree.Session')),
            ],
            options={
                'db_table': 'beec_mg_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('prob', otree.db.models.IntegerField(null=True)),
                ('endowment', otree.db.models.CurrencyField(default=0, null=True)),
                ('contribution', otree.db.models.CurrencyField(default=0, null=True, verbose_name='Deslice hasta seleccionar la cantidad a enviar deseada')),
                ('counter', otree.db.models.IntegerField(default=1, null=True)),
                ('roller', otree.db.models.IntegerField(null=True, verbose_name='Deslice hasta seleccionar el número de la opción deseada')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beec_mg.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beec_mg_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beec_mg_player', to='otree.Session')),
            ],
            options={
                'db_table': 'beec_mg_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beec_mg_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'beec_mg_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beec_mg.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beec_mg.Subsession'),
        ),
    ]