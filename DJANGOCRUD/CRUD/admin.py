from django.contrib import admin
from .models import App_Users
# Register your models here.

@admin.register(App_Users)
class User_admin(admin.ModelAdmin):
    list_display= ['id','First_Name','Last_name','email','password','confirm_Password']