from django.db import models
from django.urls import reverse


# Create your models here.
class Gallerys(models.Model):
	name = models.CharField(max_length = 300)
	url = models.URLField()
	typ = models.CharField(max_length = 300)
	direct_url = models.URLField()
	site_name = models.CharField(max_length = 300)
	pics = models.ImageField()
	thumbnail = models.URLField()
	def __str__(self):
		return self.name

class Best_sites(models.Model):
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to = 'best_sites_img')
	content = models.TextField(max_length=200)
	slug = models.SlugField()
	url = models.URLField()
	def __str__(self):
		return self.text
	def get_absolute_url(self):
		return reverse('best_sites', kwargs = {'slug': self.slug})

class FHG_models(models.Model):
	name = models.CharField(max_length = 300)
	url = models.URLField()
	thumbnail = models.URLField()
	direct_url = models.URLField()
	
	def __str__(self):
		return self.name



