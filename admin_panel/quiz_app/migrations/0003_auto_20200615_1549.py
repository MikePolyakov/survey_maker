# Generated by Django 3.0.6 on 2020-06-15 15:49

from django.db import migrations
import fontawesome_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_answer_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='icon',
            field=fontawesome_5.fields.IconField(blank=True, max_length=60, null=True),
        ),
    ]