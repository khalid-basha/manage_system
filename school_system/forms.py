from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('user_type','mobile_num','birth_date', )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('user_type','mobile_num','birth_date', )
