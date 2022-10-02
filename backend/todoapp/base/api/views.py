from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import User, Category, Todo
from .serializers import UserSerializer, CategorySerializer, TodoSerializer
@api_view(['GET'])
def getRoutes(Request):
    routes = [
        'GET / api/users',
    ]
    return Response(routes)

@api_view([])
def getUsers(Request):
    if Request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getUser(Request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getUserCategories(Request, pk):
    categories = Category.objects.filter(user = pk)

    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUserTodos(Request, pk):
    todos = Todo.objects.filter(user = pk)

    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUserTodo(Request, pk):
    todos = Todo.objects.filter(user = pk)

    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)