from django.db import models

# Create your models here.
# main/models.py
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=120)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class CategoryItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.category.title} - {self.title}"
