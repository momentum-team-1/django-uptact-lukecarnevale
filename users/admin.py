from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# , Contact
# , Address

admin.site.register(User, UserAdmin)
# admin.site.register(Contact)
# admin.site.register(Address)