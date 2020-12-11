from django.db import models

# ORM

class ArticleCard(models.Model):
	"""Карточки статьей"""
	title = models.CharField('название статьи', max_length=200)
	link = models.CharField('ссылка на статью', max_length=100)
	photo_link = models.CharField('ссылка на фото', max_length=100)
	
	class Meta:
		verbose_name = 'Карточку'
		verbose_name_plural = 'Карточки'

class HeadArticleCard(models.Model):
	"""Карточки статьей размещенных на главной странице"""
	article_card = models.ForeignKey(ArticleCard, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Карточку на главной странице'
		verbose_name_plural = 'Карточки на главной странице'
