# Generated by Django 3.0.6 on 2020-05-28 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies_app', '0001_initial'),
        ('surveys_app', '0003_auto_20200528_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='company',
        ),
        migrations.AddField(
            model_name='survey',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies_app.Company'),
        ),
    ]