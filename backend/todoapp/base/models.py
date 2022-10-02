from django.db import models
from django.db.models import Q
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, null=True, unique=True)

    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS: []

class Category(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    note = models.TextField(max_length=200, null=True, blank=True)
    group = models.ForeignKey(Category, on_delete=models.CASCADE,
                                # limit_choices_to={'user': 1},
                                null=True, blank=True)
    created = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.title
