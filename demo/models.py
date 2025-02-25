from django.db import models

# Create your models here.

class Query(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=300)

    def __str__(self):
        return self.name

#creating database model for notice board 

class Notice(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expiry_date = models.DateTimeField(null=True, blank=True)
    attachments = models.FileField(upload_to='Notice/', null=True,blank=True)

    def __str__(self):
        return self.title 
    

    