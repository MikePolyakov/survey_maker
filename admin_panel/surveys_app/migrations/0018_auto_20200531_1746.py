# Generated by Django 3.0.6 on 2020-05-31 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys_app', '0017_auto_20200531_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='info_pages',
        ),
        migrations.AddField(
            model_name='namedpages',
            name='survey',
            field=models.ManyToManyField(blank=True, to='surveys_app.Survey'),
        ),
    ]