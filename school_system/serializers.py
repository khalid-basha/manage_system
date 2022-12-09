from rest_framework import serializers
from .models import User as CustomUser, Teacher, Student, Course
from django.contrib.auth.models import AbstractUser

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'subject', 'hours','teacher_id')

    def create(self, validated_data):
        """
        Create and return a new `Course` instance, given the validated data.
        """
        if self.context['teacher']:
            teacher = self.context['teacher']
            validated_data['teacher_id'] = teacher.user.id
        course= Course.objects.create(**validated_data)
        return course


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        write_only_fields = ('password',)

    def create(self, validated_data):
        user= CustomUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('user',)
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        teacher = Teacher.objects.create(user=user, **validated_data)
        return teacher

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('user', 'courses')
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student
