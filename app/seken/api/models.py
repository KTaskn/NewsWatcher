from django.db import models

class Newspaper(models.Model):
    name = models.CharField(max_length=20)

class Word(models.Model):
    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    _datetime = models.DateTimeField()
    