from django.db import models

class Article(models.Model):
    # article model
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return (self.title)
