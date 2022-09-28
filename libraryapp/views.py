from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import api_view
from libraryapp.serializers import UserSerializer, GroupSerializer, BookSerializer, AdminRegistrationSerializer, UserRegistrationSerializer, UserLoginSerializer, BookGetAllSerializer, AdminLoginSerializer
from rest_framework.response import Response
from libraryapp.models import Book, AdminRegistration, UserRegistration

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['POST'])
def add_book(request):
    Email = dict(request.data)['Email'][0]
    Password = dict(request.data)['Password'][0]
    serializer = BookSerializer(data = request.data)
    # serializer = UserLoginSerializer(data = request.data)
    try:
        Password1 = list(AdminRegistration.objects.filter(Email = Email).values())[0]['Password']
        if Password1 == Password:
            if serializer.is_valid():
                serializer.save()
                return Response({"Status":"Added"},status= status.HTTP_201_CREATED)
    except:
        return Response({"Status":"Email ID not found"}, status = status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register_new_admin(request):
    serializer = AdminRegistrationSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Status":"Added"},status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_new_admin(request):
    Email = dict(request.data)['Email'][0]
    Password = dict(request.data)['Password'][0]
    try:
        Password1 = list(AdminRegistration.objects.filter(Email = Email).values())[0]['Password']
        if Password1 == Password:
            return Response({"Status":"Successfull"},status= status.HTTP_201_CREATED)
        else:
            return Response({"Status":"Failed"}, status = status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"Status":"Email ID not found"}, status = status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register_new_user(request):
    serializer = UserRegistrationSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Status":"Added"},status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_new_user(request):
    Email = dict(request.data)['Email'][0]
    Password = dict(request.data)['Password'][0]
    try:
        Password1 = list(UserRegistration.objects.filter(Email = Email).values())[0]['Password']
        if Password1 == Password:
            return Response({"Status":"Successfull"},status= status.HTTP_201_CREATED)
        else:
            return Response({"Status":"Failed"}, status = status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"Status":"Email ID not found"}, status = status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_books_by_user(request):
    Email = dict(request.data)['Email'][0]
    Password = dict(request.data)['Password'][0]
    try:
        Password1 = list(UserRegistration.objects.filter(Email = Email).values())[0]['Password']
        if Password1 == Password:
            charities = Book.objects.all().order_by('-BookId')
            serializer2 = BookGetAllSerializer(charities, many = True)
            return Response(serializer2.data)
        else:
            return Response({"Status":"Failed"}, status = status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"Status":"Email ID not found"}, status = status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_books_by_admin(request):
    Email = dict(request.data)['Email'][0]
    Password = dict(request.data)['Password'][0]
    try:
        Password1 = list(AdminRegistration.objects.filter(Email = Email).values())[0]['Password']
        if Password1 == Password:
            charities = Book.objects.all().order_by('-BookId')
            serializer2 = BookGetAllSerializer(charities, many = True)
            return Response(serializer2.data)
        else:
            return Response({"Status":"Failed"}, status = status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"Status":"Email ID not found"}, status = status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def modify_book_details(request):
    Email = dict(request.data)['Email'][0]
    Password = dict(request.data)['Password'][0]
    BookId = dict(request.data)['BookId'][0]
    BookName = dict(request.data)['BookName'][0]
    Author = dict(request.data)['Author'][0]
    # serializer = UserLoginSerializer(data = request.data)
    try:
        Password1 = list(AdminRegistration.objects.filter(Email = Email).values())[0]['Password']
        if Password1 == Password:
            Book.objects.filter(BookId=BookId).update(BookName = BookName , Author=Author)
            return  Response({"Status":"Modified"},status=status.HTTP_201_CREATED)
        else:
            return Response({"Status":"Failed"}, status = status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"Status":"Email ID not found"}, status = status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_item(request):
    Email = dict(request.data)['Email'][0]
    Password = dict(request.data)['Password'][0]
    BookId = dict(request.data)['BookId'][0]
    try:
        Password1 = list(AdminRegistration.objects.filter(Email = Email).values())[0]['Password']
        if Password1 == Password:
            Book.objects.get(BookId=BookId).delete()
            return Response({"Status": "Delted"}, status=status.HTTP_200_OK)
        else:
            return Response({"Status":"Failed"}, status = status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"Status":"Email ID not found"}, status = status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
