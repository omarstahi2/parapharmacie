# Generated by Django 3.2.12 on 2024-04-21 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_remove_cartitem_variations'),
        ('store', '0006_variation_is_active'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Variation',
        ),
    ]
