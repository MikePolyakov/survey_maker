from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Название')
    logo = models.ImageField(null=True, blank=True, upload_to='company_logo', verbose_name='Логотип')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'компании'

    def __str__(self):
        return self.name


class Department(MPTTModel):
    department_name = models.CharField(max_length=64, unique=True, verbose_name='Подразделение')
    head_of_department = models.CharField(max_length=64, null=True, blank=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    workers = models.PositiveIntegerField(null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    class MPTTMeta:
        order_insertion_by = ['department_name']

    def __str__(self):
        return self.department_name
