from django.shortcuts import render
from school_system.forms import CustomUserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import generic
from .models import Teacher, Student

# Create your views here.
def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        import pdb; pdb.set_trace()
        form = CustomUserCreationF< orm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.user_type == 2:
                Student.objects.create(user=user)
            elif user.user_type == 3:
                Teacher.objects.create(user=user)
            login(request, user)
            return render(request, "users/dashboard.html")

# class SignUp(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'
