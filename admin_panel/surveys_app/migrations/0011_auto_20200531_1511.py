# Generated by Django 3.0.6 on 2020-05-31 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys_app', '0010_auto_20200531_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]