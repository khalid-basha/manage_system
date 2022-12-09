from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
class UserAdmin(UserAdmin):
    add_form= CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    add_fieldsets = UserAdmin.add_fieldsets +(
        (None, {'fields': ('user_type','birth_date')}),
    )

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
