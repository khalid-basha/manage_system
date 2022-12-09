from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField
from django.conf import settings

class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(format=settings.DATE_INPUT_FORMATS),
        input_formats=settings.DATE_INPUT_FORMATS,
    )
    user_type= forms.CharField(label='You are a?', widget=forms.RadioSelect(choices=[(2,'STUDENT'),
    (3,'TEACHER'),]))
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email','birth_date','user_type','mobile_num',)
    def save(self, commit = True):
        import pdb; pdb.set_trace()
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email','user_type','mobile_num','birth_date', )
