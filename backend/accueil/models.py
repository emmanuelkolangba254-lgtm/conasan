from django.db import models

class Hero(models.Model):

    titre = models.CharField(max_length=255)

    description = models.TextField()

    image = models.ImageField(
        upload_to='hero/'
    )

    def __str__(self):
        return self.titre
# Create your models here.
