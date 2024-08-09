from django.db import models

class Topic(models.Model):
    topic_name = models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_name 

class Webpage(models.Model):
    topic_name = models.ForeignKey('Topic',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url=models.URLField()
    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    name = models.ForeignKey('Webpage',on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return str(self.date)
    
# Create your models here.