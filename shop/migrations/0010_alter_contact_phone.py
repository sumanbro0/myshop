# Generated by Django 3.2.9 on 2021-11-27 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]