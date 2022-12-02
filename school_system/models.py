from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from .managers import UserManager
# Create your models here.


class User(AbstractUser):
    USER_TYPE_OPTIONS = (
        (1,'ADMIN'),
        (2,'STUDENT'),
        (3,'TEACHER'),
    )
    user_type = models.PositiveSmallIntegerField(choices = USER_TYPE_OPTIONS)
    mobile_num = PhoneNumberField(max_length =12, unique = True, null =True)
    birth_date = models.DateField(null = True)
    objects = UserManager()
    def __str__(self):
        return self.username


class Teacher( models.Model):
    user = models.OneToOneField(get_user_model(), on_delete = models.CASCADE, primary_key = True)

class Course(models.Model):
    title = models.CharField(max_length = 191)
    teacher = models.ForeignKey(Teacher, null= True, on_delete=models.SET_NULL)

class Student( models.Model):
    user = models.OneToOneField(get_user_model(), on_delete = models.CASCADE, primary_key = True)
    courses = models.ManyToManyField(Course)
