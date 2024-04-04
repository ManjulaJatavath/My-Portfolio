from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(blank=True, null=True)
    phone=models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name

    