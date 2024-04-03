from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Label(models.Model):
    name = models.CharField(max_length=50, unique=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name


completion_status_option = (
    ('',''),
    ('pending', 'pending'),
    ('completed', 'complete')
)


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completion_status = models.CharField(max_length=100, choices=completion_status_option, default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.ManyToManyField(Label, related_name='Label', default=None)
    def __str__(self):
        return self.title
