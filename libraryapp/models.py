from django.db import models

# Create your models here.
class Book(models.Model):
    BookId = models.AutoField(primary_key=True,default=None)
    BookName = models.CharField(max_length=200)
    Author = models.CharField(max_length=200) # Default isliye diya h because ye wala pehle se bana tha aur field change kiya apanne usska


    def __str__(self):
        return str(self.BookId)

class AdminRegistration(models.Model):
    Email = models.EmailField(unique = True)
    AdminName = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)

    def __str__(self):
        return self.AdminName

class UserRegistration(models.Model):
    Email = models.EmailField(unique = True)
    UserName = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)

    def __str__(self):
        return self.UserName
