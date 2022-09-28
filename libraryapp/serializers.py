from django.contrib.auth.models import User, Group
from rest_framework import serializers
from libraryapp.models import Book,AdminRegistration, UserRegistration


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['BookId','BookName','Author']

class AdminRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdminRegistration
        fields = ['Email','Password','AdminName']

class UserRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['Email','UserName','Password']

class AdminLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdminRegistration
        fields = ['Email','Password']

class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['Email','Password']

class BookGetAllSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['BookId','BookName','Author']
