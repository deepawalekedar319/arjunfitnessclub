from django.db import models

class AllImages(models.Model):
    imageInformation = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images')

    def __str__(self) -> str:
        return self.imageInformation

class MoreImages(models.Model):
    title = models.CharField(max_length=126)
    image = models.ImageField(upload_to='images')       
    
    def __str__(self) -> str:
        return self.title

class MyImages(models.Model):
    title = models.CharField(max_length=126)
    image = models.ImageField(upload_to='images')       
    
    def __str__(self) -> str:
        return self.title