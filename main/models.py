from django.db import models


class Citie(models.Model):
	name = models.CharField(max_length = 100, verbose_name = 'Город')


	class Meta:
		verbose_name = 'Город'
		verbose_name_plural = 'Города'


	def __str__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length = 100, verbose_name = 'Категория')


	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


	def __str__(self):
		return self.name


class News_Article(models.Model):
	title = models.CharField(max_length = 100, verbose_name = 'Заголовок')
	subtitle = models.CharField(max_length = 300, verbose_name = 'Подзаголовок')
	text = models.TextField(verbose_name = 'Текст статьи')
	pub_date = models.DateTimeField(auto_now_add = True)
	citie = models.ForeignKey(Citie, on_delete = models.PROTECT, verbose_name = 'Город')
	category = models.ForeignKey(Category, on_delete = models.PROTECT, verbose_name = 'Категория')


	class Meta:
		verbose_name = 'Новостная статья'
		verbose_name_plural = 'Новостные статьи'
		ordering = ['-pub_date']


	def __str__(self):
		return self.title