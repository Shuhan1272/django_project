from django.db import models

# Create your models here.

class Query(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    