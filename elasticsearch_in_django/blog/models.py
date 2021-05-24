from django.db import models
from django.utils.text import slugify


class Post(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='post_image')
	body = models.TextField(blank=True, null=True)
	order = models.IntegerField(blank=True, null=True)
	slug = models.SlugField(default='', blank=True)

	def save(self):
		self.slug = slugify(self.title)
		super(Post, self).save()

	def __str__(self):
		return self.title
