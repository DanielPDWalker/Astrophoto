# Generated by Django 3.0.8 on 2020-07-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_system_objects', '0002_auto_20200728_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarsystemobject',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='solar_system_objects'),
        ),
    ]
