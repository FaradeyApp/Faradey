# Generated by Django 4.2.2 on 2023-07-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_avatar_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='staff'),
        ),
    ]
