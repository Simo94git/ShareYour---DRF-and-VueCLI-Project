from django.db import models
from django.conf import settings

class Article(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=240)
	content = models.TextField(null=True, blank=True) #richiesto dal frontend, modifica in seguito
	image = models.ImageField(null=True, blank=True)
	slug = models.SlugField(max_length=240, unique=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL,
								on_delete=models.CASCADE,
								related_name="articles")

	likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
								related_name="likes")

	def __str__(self):
		return self.title

class Comment(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	comment = models.CharField(max_length=5000)
	author = models.ForeignKey(settings.AUTH_USER_MODEL,
								on_delete=models.CASCADE)
	article = models.ForeignKey(Article,
								 on_delete=models.CASCADE,
								 related_name="comments") #sarebbe "comments"

	voters = models.ManyToManyField(settings.AUTH_USER_MODEL,
								related_name="votes")

	def __str__(self):
		return self.author.username