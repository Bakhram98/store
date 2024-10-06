from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    discribtion = models.TextField()


# Create your models here.
