# Generated by Django 4.1.7 on 2023-05-22 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0020_rename_quantity_basket_quanity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='user',
        ),
    ]
