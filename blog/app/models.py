from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=100)
    #author=models.CharField(max_length=20)
    author=models.ForeignKey(User, on_delete=models.DO_NOTHING) #idf user deleted what to del post models.CASCADE
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now)

def __str__(self):
    return self.author