from django.db import models

# Create your models here.

class Cakes(models.Model):
    title = models.CharField(max_length=100)
    available_size = models.CharField(max_length= 250)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='cakes/%Y/%m/%d',
                              blank=True)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
