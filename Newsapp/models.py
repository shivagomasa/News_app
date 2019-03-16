from django.db import models

# Create your models here.

class Categories(models.Model):
    class Meta:
        verbose_name_plural ='Categories'

    category = models.CharField(max_length=79)

    def __str__(self):
        return self.category

