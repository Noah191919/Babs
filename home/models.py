from django.db import models

# Create your models here.

class Testimonies(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    job = models.CharField(max_length=250, null=True, blank=True)
    testimony = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    ventes = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class AboutMe(models.Model):
    name = 'My Description'
    text1 = models.TextField(max_length=1000, null=True, blank=True)
    text2 = models.TextField(max_length=1000, null=True, blank=True)
    text3 = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name
    