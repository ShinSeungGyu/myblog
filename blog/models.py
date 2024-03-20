from django.db import models

class Post(models.Model):
    id = models.IntegerField()
    title = models.CharField(max_length=30)
    author = models.ForeignKey()
    contents = models.TextField()
    created_DT = models.DateField(auto_now_add=True)
    updated_DT = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
