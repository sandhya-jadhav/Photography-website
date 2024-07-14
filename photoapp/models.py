from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='photos/')
    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title if self.title else 'Photo {}'.format(self.id)

