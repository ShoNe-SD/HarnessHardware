# Generated by Django 4.2.5 on 2023-09-28 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_products_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='thumbnails',
            new_name='thumbnail',
        ),
    ]
