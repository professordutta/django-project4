from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=50)

    def __str__(self):
        return self.subject