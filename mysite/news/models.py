from django.db import models
from django.urls import reverse
# Create your models here.
# поля таблицы, валидации и используемые в формах
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Содержимое')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True,  verbose_name='Категория')

    def __str__(self):
        return f'{self.title}: {self.content}'

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Категория")

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return f'{self.title}'