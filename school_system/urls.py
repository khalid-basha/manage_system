from django.urls import path, include
from .views import register,courses_list,my_courses, add_course,get_course, enroll_course

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
    path("courses_list/", courses_list, name="courses_list"),
    path("courses/", my_courses, name="my_courses"),
    path("add_course/", add_course, name="add_course"),
    path("courses/<int:pk>/", get_course, name="get_course"),
    path("enroll_course/<int:pk>/", enroll_course, name="enroll_course"),
]
