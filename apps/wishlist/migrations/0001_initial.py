# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginreg', '0003_user_date_hire'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=30)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginreg.User')),
                ('wishlist_item', models.ManyToManyField(related_name='ManyUsers', to='loginreg.User')),
            ],
        ),
    ]
