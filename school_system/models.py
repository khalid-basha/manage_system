from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class UserManager(UserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('username for user must be set')
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.user_type = 1
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

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
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

class Course(models.Model):
    title = models.CharField(max_length = 191)
    teacher = models.ForeignKey(Teacher, null= True, on_delete=models.SET_NULL)

class Student( models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    courses = models.ManyToManyField(Course)
