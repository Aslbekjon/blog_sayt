from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 200)
    slug = models.SlugField(unique = True)
    img = models.ImageField(upload_to='blog/', default = True)
    description = models.TextField()

    def __str__(self):
        return self.name