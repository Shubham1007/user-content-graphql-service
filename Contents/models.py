from django.db import models
from django.utils.timezone import now


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.name


class Content(models.Model):
    heading = models.CharField(max_length=100)
    content_data = models.TextField()
    created_at = models.DateField(default=now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.heading
