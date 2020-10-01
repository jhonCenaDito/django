from django.db import models

# Create your models here.

class Post(models.Model):
    class Meta:
        verbose_name_plural = "Post"
    name = models.CharField(max_length = 32)

    def __str__(self):
        return self.name



class Player(models.Model):
    name = models.CharField(max_length = 20)
    description = models.TextField()
    post = models.ForeignKey(Post, on_delete = models.CASCADE)

    def __str__(self):
        return self .name
        