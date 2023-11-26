from django.db import models

# Create your models here.
class pizza(models.Model):
    name = models.CharField(max_length=200)
    ingridients = models.CharField(max_length=400)
    price = models.FloatField(default=0)
    vegetarian= models.BooleanField(default=False)

    def __str__(self):
        return self.name