from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(blank=True, null=True)
    phone=models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name

class Blogs(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField()
    authname=models.CharField(max_length=25)
    img=models.ImageField(upload_to='blogs',blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title   