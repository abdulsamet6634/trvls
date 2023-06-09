# Generated by Django 4.1.7 on 2023-05-19 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0015_countries'),
    ]

    operations = [
        migrations.AddField(
            model_name='countries',
            name='continents_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.continents', verbose_name='kıta'),
        ),
        migrations.AlterField(
            model_name='countries',
            name='img',
            field=models.ImageField(max_length=500, upload_to='None', verbose_name='ülke bayrağı resmi'),
        ),
    ]
