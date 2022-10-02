from django.contrib import admin
# Register your models here.
from .models import User, Category, Todo

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Todo)