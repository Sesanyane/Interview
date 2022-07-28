from django.contrib.auth.models import Group
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.views.generic import TemplateView


def group_check(request):
    group_name = Group.objects.all().filter(
        user=request.user)  # get logget user grouped name
    group_name = str(group_name[0])  # convert to string

    if "Student" == group_name:
        return redirect('http://127.0.0.1:8000/student/')
    elif "Teacher" == group_name:
        return redirect('http://127.0.0.1:8000/teacher/')


def logout_view(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')


class register_teacher(TemplateView):
    template_name = "register_teacher.html"


class register_student(TemplateView):
    template_name = "register_student.html"
