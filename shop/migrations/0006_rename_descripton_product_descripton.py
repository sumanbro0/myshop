# Generated by Django 3.2.9 on 2021-11-05 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_descripton_product_descripton'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descripton',
            new_name='Descripton',
        ),
    ]
