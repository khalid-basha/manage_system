from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from .managers import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

USER_TYPES_OPTIONS = (
        (1,'ADMIN'),
        (2,'STUDENT'),
        (3,'TEACHER'),
    )

class User(AbstractUser):
    """Custom User model with additional fields and user type options."""
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPES_OPTIONS)
    mobile_num = PhoneNumberField(max_length =13, unique = True, null =True)
    birth_date = models.DateField(null =True, default = "1999-09-09")
    objects = UserManager()

    def __str__(self):
        return self.username

class Teacher( models.Model):
    """Teacher model with a one-to-one relationship with the User model."""
    user = models.OneToOneField(get_user_model(), on_delete = models.CASCADE,
            primary_key = True)

class Course(models.Model):
    """Course model with a title, subject, hours, and a teacher."""
    title = models.CharField(max_length = 191)
    subject = models.CharField(max_length = 191)
    hours = models.PositiveIntegerField(default=0 )
    teacher = models.ForeignKey(Teacher, null= True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.title

class Student( models.Model):
    """Student model with a one-to-one relationship with the User model and a
    many-to-many relationship with the Course model."""
    user = models.OneToOneField(get_user_model(), on_delete = models.CASCADE,
            primary_key = True)
    courses = models.ManyToManyField(Course, related_name='enrolled_students')

@receiver(post_save, sender=User)
def user_specifying(sender, instance, created, **kwargs):
    if created:
        user_type = instance.user_type
        if user_type == 2:
            student = Student(user= instance)
            student.save()
        elif user_type == 3:
            teacher = Teacher(user= instance)
            teacher.save()
