from django.shortcuts import render
from school_system.forms import CustomUserCreationForm
from django.contrib.auth import login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import User,Course, Student, Teacher
from .serializers import UserSerializer, CourseSerializer
from django.contrib.auth.decorators import login_required

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return JsonResponse(serializer.data, status=201)
    return JsonResponse({'error': 'Invalid data'}, status=400)

@csrf_exempt
def courses_list(request):
    if request.method == "GET":
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse({"Error": "405 Method Not Allowed"}, status=405)

@csrf_exempt
@login_required(login_url='/accounts/login/')
def my_courses(request):
    if request.user.user_type == 2:
        courses = Student.objects.get(user=request.user).courses
        return get_courses(courses, "No courses found for student")
    elif request.user.user_type == 3:
        courses = Course.objects.filter(teacher_id=request.user.id)
        return get_courses(courses, "No courses found for teacher")
    else:
        return JsonResponse({"Error": "Invalid user type"}, status=406)

def get_courses(courses, error_msg):
    if courses.exists():
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({"Error": error_msg}, status=404)


def get_course(request, pk):
    if request.method == "GET":
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course)
        return JsonResponse(serializer.data)
    else:
        return JsonResponse({"Error": "Method Not Allowed"}, status=405)

@csrf_exempt
@login_required(login_url='/accounts/login/')
def add_course(request):
    if request.method == "POST":
        if request.user.user_type == 3:
            data = JSONParser().parse(request)
            teacher = Teacher.objects.get(pk=request.user.id)
            serializer = CourseSerializer(data=data, context={"teacher": teacher})
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"result": "course created"}, status=201)
            return JsonResponse(serializer.errors, status=400)
        return JsonResponse({'error': 'Only teachers can add courses'}, status=401)
    return JsonResponse({"Error": "Method Not Allowed"}, status=405)

@csrf_exempt
@login_required(login_url='/accounts/login/')
def enroll_course(request, pk):
    if request.method == "POST":
        if request.user.user_type == 2:
            student = Student.objects.get(user=request.user)
            course = Course.objects.get(pk=pk)
            student.courses.add(course)
            return JsonResponse({'message': 'Successfully enrolled in course'})
        return JsonResponse({'error': 'Only students can enroll in courses'}, status=401)
    return JsonResponse({"Error": "Method Not Allowed"}, status=405)
