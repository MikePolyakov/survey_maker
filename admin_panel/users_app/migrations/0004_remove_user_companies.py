# Generated by Django 3.0.6 on 2020-05-11 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0003_auto_20200511_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='companies',
        ),
    ]
