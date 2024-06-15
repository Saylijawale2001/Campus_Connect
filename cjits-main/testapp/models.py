from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=1000)
class Message(models.Model):
    value=models.CharField(max_length=10000000)
    date=models.DateTimeField(default=datetime.now, blank=True)
    user=models.CharField(max_length=10000000)
    room=models.CharField(max_length=1000000)
#model that upload any type of document  
class Document(models.Model):
    filename=models.CharField(max_length=300,default=True)
    subject=models.CharField(max_length=300,default=True)
    title=models.CharField(max_length=300,default=True)
    semister=models.CharField(default=True,max_length=300)
    file=models.FileField(upload_to='documents/')
    
#Model that to upload Video
class Video(models.Model):
    filename=models.CharField(default=None,max_length=200)
    description=models.TextField()
    video_file = models.FileField(upload_to='videos/')
#model for the links provides to learning
class Links(models.Model):
    program=models.CharField(default=True,max_length=200)
    fullstack=models.CharField(default=True,max_length=200)
    cybersecurity=models.CharField(default=True,max_length=200)
    ai=models.CharField(default=True,max_length=200)
    ml=models.CharField(default=True,max_length=200)
    robotics=models.CharField(default=True,max_length=200)
    datascience=models.CharField(default=True,max_length=200)

class Notify(models.Model):
    text=models.TextField()
    
    
    