from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    number_of_pages = models.IntegerField()
    author = models.CharField(max_length=128)
    quantity = models.IntegerField()
    published = models.DateField(auto_now_add=True)
    
    @property
    def my_field(self):
        return None

    def __str__(self):
        return self.title
