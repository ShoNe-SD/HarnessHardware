# Generated by Django 4.2.5 on 2023-09-28 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
