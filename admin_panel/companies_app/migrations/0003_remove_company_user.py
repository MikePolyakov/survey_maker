# Generated by Django 3.0.6 on 2020-05-11 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies_app', '0002_company_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='user',
        ),
    ]
