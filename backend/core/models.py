from django.db import models
class Programme(models.Model):

    titre = models.CharField(max_length=200)

    description = models.TextField()

    image1 = models.ImageField(upload_to="programmes/")

    image2 = models.ImageField(upload_to="programmes/", blank=True, null=True)

    image3 = models.ImageField(upload_to="programmes/", blank=True, null=True)

    image4 = models.ImageField(upload_to="programmes/", blank=True, null=True)

    def __str__(self):
        return self.titre

# Create your models here.
