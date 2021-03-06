# Generated by Django 4.0 on 2021-12-23 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=90)),
                ('address', models.CharField(max_length=90)),
                ('city', models.CharField(max_length=90)),
                ('state', models.CharField(max_length=90)),
                ('zip', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]
