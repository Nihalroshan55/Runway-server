# Generated by Django 4.2.3 on 2023-10-15 19:07

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hub',
            name='hub_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='hub',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326, unique=True),
        ),
    ]