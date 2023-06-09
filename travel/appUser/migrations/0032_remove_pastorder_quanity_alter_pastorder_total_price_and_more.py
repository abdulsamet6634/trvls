# Generated by Django 4.1.7 on 2023-05-23 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0050_remove_userinfo_order_date'),
        ('appUser', '0031_pastorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pastorder',
            name='quanity',
        ),
        migrations.AlterField(
            model_name='pastorder',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='pastorder',
            name='tuors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.tour'),
        ),
    ]
