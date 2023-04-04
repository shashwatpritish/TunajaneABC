from django.db import models

# Create your models here.
class Text(models.Model):
    word = models.CharField(max_length=5000,null=False)
    def __str__(self):
        return self.word

class Contact(models.Model):
    name = models.CharField(max_length=5000,null=False)
    email = models.EmailField(max_length=5000,null=False)
    message = models.TextField(max_length=5000,null=False)
    def __str__(self):
        return f"{self.name}"