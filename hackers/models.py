from django.db import models
from account.models import User

# Create your models here.
class Link(models.Model):
	title = models.CharField(max_length=200, verbose_name='عنوان')
	url = models.URLField(verbose_name='آدرس')
	description = models.TextField(verbose_name='توضیحات')
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
	vote = models.IntegerField(verbose_name='رای', default=0)

	class Meta:
		verbose_name = 'آدرس'
		verbose_name_plural = 'آدرس ها'

	def __str__(self):
		return "{} - {}".format(self.title, self.user)