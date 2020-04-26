from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
	#add_form =  form per la creazione
	#form =    form per la modifica
	model = CustomUser
	list_display = ["username", "email", "is_staff"]



admin.site.register(CustomUser, CustomUserAdmin)