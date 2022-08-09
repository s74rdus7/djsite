from django.db import models
from django.urls import reverse

class PLACES(models.Model):
    username = models.CharField(max_length=255, verbose_name='Логин')
    gmail = models.CharField(max_length=255, verbose_name='Почта')
    password1 = models.CharField(max_length=255, verbose_name='Пароль')
    password2 = models.CharField(max_length=255, verbose_name='Повторите пароль')
    PLACE_NAME = models.CharField(max_length=255, verbose_name='Название учреждения')
    PLACE_ADRES = models.CharField(max_length=255, verbose_name='Адрес')
    FIO_DIR = models.CharField(max_length=255, verbose_name='ФИО Директора учреждения')
    PLACE_CONTACT_NUMBER = models.CharField(max_length=255, verbose_name='Контактный номер')
    DOCUMENTS_DLYA_PRIEMA = models.CharField(max_length=255, verbose_name='Документы для приема')
    PLACE_PHOTO = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото учреждения')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.PLACE_NAME

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def get_employees(self):
        return reverse('show_employees', kwargs={'Svyaz_slug': self.slug})

    def get_event(self):
        return reverse('show_events', kwargs={'Svyaz_slug': self.slug})

    class Meta:
        verbose_name = 'Учреждения'
        verbose_name_plural = 'Учреждения'
        ordering = ['PLACE_NAME']

class Employees(models.Model):
    FIRST_NAME = models.CharField(max_length=255, verbose_name='Имя')
    LAST_NAME = models.CharField(max_length=255, verbose_name='Фамилия')
    IIN = models.CharField(max_length=255, verbose_name='ИИН')
    WORK_PLACE = models.TextField(blank=True, verbose_name='Место работы')
    JOB_TITLE = models.TextField(blank=True, verbose_name='Должность')
    PHOTO_3x4 = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото 3х4')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать')
    Svyaz = models.ForeignKey('PLACES', on_delete=models.PROTECT, verbose_name='Повторить место работы')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')


    def __str__(self):
        return self.FIRST_NAME

    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'
        ordering = ['FIRST_NAME']

class Events(models.Model):
    EVENT_NAME = models.CharField(max_length=255, verbose_name='Название события')
    EVENT_CREATER = models.CharField(max_length=255, verbose_name='Организатор')
    PROTOCOL = models.CharField(max_length=255, verbose_name='Протокол')
    DATE_START = models.CharField(max_length=255, verbose_name='Дата начала')
    DATE_END = models.CharField(max_length=255, verbose_name='Дата окончания')
    PHOTO_FROM_EVENT = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото с события')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    Svyaz = models.ForeignKey('PLACES', on_delete=models.PROTECT, verbose_name='Повторите организатора')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')


    def __str__(self):
        return self.EVENT_NAME

    class Meta:
        verbose_name = 'События'
        verbose_name_plural = 'События'
        ordering = ['EVENT_NAME']