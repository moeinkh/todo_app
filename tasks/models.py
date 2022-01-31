from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    class Meta:
        verbose_name = 'کار'
        verbose_name_plural = 'کار ها'
        ordering = ['-created']

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')    

    title = models.CharField('عنوان', max_length=64)
    active = models.BooleanField('فعال؟', default=True)

    created = models.DateTimeField('تاریخ ایجاد', auto_now_add=True)

    def __str__(self):
        return self.title    