from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(model.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)#the title has a max length of 200 chars
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()#self represents the instance of the class, by using ir we can acess the attributes and methods defined in the 
        self.save()
    

    def __str__(self):
        return self.title
