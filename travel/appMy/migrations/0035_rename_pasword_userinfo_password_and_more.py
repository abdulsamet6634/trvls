# Generated by Django 4.1.7 on 2023-05-21 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0034_userinfo_delete_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='pasword',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='user',
            new_name='username',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.CharField(max_length=50, null=True, verbose_name='email'),
        ),
    ]