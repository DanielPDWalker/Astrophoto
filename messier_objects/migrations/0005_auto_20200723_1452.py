# Generated by Django 2.2.9 on 2020-07-23 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messier_objects', '0004_auto_20200723_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messierobject',
            name='photo',
            field=models.ImageField(blank=True, default='notcaptured.JPG', null=True, upload_to='messier_objects'),
        ),
    ]
