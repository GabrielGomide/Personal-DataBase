from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(auto_now=False, auto_now_add=False, null=True)
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=50)
    instagram = models.CharField(max_length=100)
    notes = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.name

    def as_list(self):
        return self.notes.split('\n')

class Note(models.Model):
    title = models.CharField(max_length=200)
    notes = models.CharField(max_length=10000)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def as_list(self):
        return self.notes.split('\n')

