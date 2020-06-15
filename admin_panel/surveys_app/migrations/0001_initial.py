# Generated by Django 3.0.6 on 2020-06-15 14:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import fontawesome_5.fields
import mptt.fields
import surveys_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', fontawesome_5.fields.IconField(blank=True, max_length=60)),
                ('name', models.CharField(max_length=64)),
                ('active_answer', models.BooleanField(default=False)),
                ('radio_buttons', models.BooleanField(default=False)),
                ('drop_down_list', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Предлагаемый вариант ответа',
                'verbose_name_plural': 'Предлагаемые варианты ответов',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField(blank=True, null=True)),
                ('page_name', models.CharField(blank=True, max_length=32)),
                ('page_help', models.CharField(blank=True, max_length=128)),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('Mono', 'Mono'), ('Poly', 'Poly'), ('Text', 'Text')], default='Mono', max_length=255)),
                ('question_title', models.CharField(blank=True, max_length=128, null=True)),
                ('question_help', models.CharField(blank=True, max_length=128, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='question_image')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('page', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='surveys_app.Page')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='surveys_app.Question')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'вопросы',
            },
        ),
        migrations.CreateModel(
            name='UserCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=surveys_app.models.random_string, max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('is_draft', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('hello_title', models.CharField(blank=True, max_length=32, null=True, verbose_name='Приветствие')),
                ('hello_text', models.TextField(blank=True, max_length=256, null=True, verbose_name='ТЕКСТ')),
                ('info_title', models.CharField(blank=True, max_length=32, null=True, verbose_name='Инструкция')),
                ('info_text', models.TextField(blank=True, max_length=256, null=True, verbose_name='ТЕКСТ')),
                ('bye_title', models.CharField(blank=True, max_length=32, null=True, verbose_name='Завершение')),
                ('bye_text', models.TextField(blank=True, max_length=256, null=True, verbose_name='ТЕКСТ')),
                ('created_day', models.DateField(default=django.utils.timezone.now)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('contacts', models.TextField(blank=True, max_length=128, null=True)),
                ('answers_counter', models.PositiveIntegerField(blank=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies_app.Company')),
                ('language', models.ManyToManyField(blank=True, default='1', to='surveys_app.Language')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'опросы',
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys_app.Answer')),
                ('code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys_app.UserCode')),
                ('question', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='surveys_app.Question')),
                ('survey', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='surveys_app.Survey')),
            ],
            options={
                'verbose_name': 'Полученный ответ',
                'verbose_name_plural': 'Полученные ответы',
            },
        ),
        migrations.AddField(
            model_name='page',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys_app.Survey'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ManyToManyField(blank=True, to='surveys_app.Question'),
        ),
    ]
