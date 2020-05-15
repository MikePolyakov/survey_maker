# Generated by Django 3.0.6 on 2020-05-15 02:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('surveys_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='returncode',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.ManyToManyField(blank=True, to='surveys_app.Answer'),
        ),
        migrations.AddField(
            model_name='question',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='surveys_app.Question'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys_app.QuestionType'),
        ),
        migrations.AddField(
            model_name='page',
            name='question',
            field=models.ManyToManyField(blank=True, to='surveys_app.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys_app.QuestionType'),
        ),
    ]