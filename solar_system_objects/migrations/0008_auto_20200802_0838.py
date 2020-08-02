# Generated by Django 3.0.8 on 2020-08-02 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_system_objects', '0007_solarsystemobject_capture_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarsystemobject',
            name='distance_from_sun_au',
            field=models.FloatField(max_length=25, null=True),
        ),
    ]