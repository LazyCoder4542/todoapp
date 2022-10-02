from rest_framework.serializers import ModelSerializer
from base.models import User, Category, Todo

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"