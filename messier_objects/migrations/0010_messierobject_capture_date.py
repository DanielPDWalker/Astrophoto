# Generated by Django 3.0.8 on 2020-07-29 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messier_objects', '0009_auto_20200728_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='messierobject',
            name='capture_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]