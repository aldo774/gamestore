# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151006_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plataforma',
            name='pagina',
            field=models.CharField(max_length=30, default='/item/'),
        ),
    ]
