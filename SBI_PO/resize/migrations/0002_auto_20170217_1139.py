# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-17 11:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resize', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='image_upload_form',
            new_name='image_upload',
        ),
        migrations.AlterModelTable(
            name='image_upload',
            table='image_upload',
        ),
    ]