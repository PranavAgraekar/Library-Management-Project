from django.contrib import admin
from libraryapp.models import Book, AdminRegistration, UserRegistration
# Register your models here.
admin.site.register(Book,)
admin.site.register(AdminRegistration,)
admin.site.register(UserRegistration,)
