import uuid

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from companies_app.models import Company
from django.utils.timezone import now
from fontawesome_5.fields import IconField


def random_string():
    return str(uuid.uuid4().hex[:5].upper())


# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.name


class Survey(models.Model):
    name = models.CharField(max_length=64)
    is_draft = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    hello_title = models.CharField(max_length=32, null=True, blank=True, verbose_name='Приветствие')
    hello_text = models.TextField(max_length=256, null=True, blank=True, verbose_name='ТЕКСТ')
    info_title = models.CharField(max_length=32, null=True, blank=True, verbose_name='Инструкция')
    info_text = models.TextField(max_length=256, null=True, blank=True, verbose_name='ТЕКСТ')
    bye_title = models.CharField(max_length=32, null=True, blank=True, verbose_name='Завершение')
    bye_text = models.TextField(max_length=256, null=True, blank=True, verbose_name='ТЕКСТ')
    created_day = models.DateField(default=now)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    contacts = models.TextField(max_length=128, null=True, blank=True)
    answers_counter = models.PositiveIntegerField(null=True, blank=True)
    language = models.ManyToManyField(Language, blank=True,  default='1')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'опросы'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('surveys:welcome', kwargs={'slug': self.slug})


class Pages(models.Model):
    number = models.SmallIntegerField(null=True, blank=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    page_name = models.CharField(max_length=32,  blank=True)
    page_help = models.CharField(max_length=128, blank=True)

    def page_number(self):
        pages = Pages.objects.filter(survey=self.survey)
        i = 1
        for page in pages:
            page.number = i
            page.save()
            i += 1
        return self.number

    def get_questions(self):
        questions = self.question_set.all()
        return questions

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class Question(MPTTModel):
    TYPE_QUESTION = (
        ("Mono", "Mono"),
        ("Poly", "Poly"),
        ("Text", "Text"),
    )
    question_type = models.CharField(max_length=255, choices=TYPE_QUESTION, default='Mono')
    question_title = models.CharField(max_length=128, null=True, blank=True)
    question_help = models.CharField(max_length=128, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='question_image')
    page = models.ForeignKey(Pages, on_delete=models.CASCADE, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'вопросы'


class Answer(models.Model):
    icon = IconField()
    question = models.ManyToManyField(Question, blank=True)
    name = models.CharField(max_length=64)
    active_answer = models.BooleanField(default=False)
    radio_buttons = models.BooleanField(default=False)
    drop_down_list = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Предлагаемый вариант ответа'
        verbose_name_plural = 'Предлагаемые варианты ответов'

    def __str__(self):
        return self.name


class UserCode(models.Model):
    code = models.CharField(max_length=5, unique=True, default=random_string)


class Response(models.Model):
    code = models.ForeignKey(UserCode, on_delete=models.CASCADE, null=True, blank=True,)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, blank=True,)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True,)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True,)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Полученный ответ'
        verbose_name_plural = 'Полученные ответы'
