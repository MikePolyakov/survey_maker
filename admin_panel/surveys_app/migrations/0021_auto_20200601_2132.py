# Generated by Django 3.0.6 on 2020-06-01 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys_app', '0020_auto_20200531_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='bye_text',
            field=models.TextField(blank=True, max_length=128, null=True, verbose_name='ТЕКСТ'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='bye_title',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='ЗАГОЛОВОК'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='hello_text',
            field=models.TextField(blank=True, max_length=128, null=True, verbose_name='ТЕКСТ'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='hello_title',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='ЗАГОЛОВОК'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='info_text',
            field=models.TextField(blank=True, max_length=128, null=True, verbose_name='ТЕКСТ'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='info_title',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='ЗАГОЛОВОК'),
        ),
    ]