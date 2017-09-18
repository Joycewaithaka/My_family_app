from django.db import models

# Create your models here.
class Myfamily (models.Model):
      name = models.CharField(max_length=200)
      position = models.TextField()
      description =models.TextField(default ="nice child")
      # def __str__(self):
      #     return self.names