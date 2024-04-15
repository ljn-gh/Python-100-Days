from django.shortcuts import render
from django.http import HttpResponse
from app.models import User


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def insertUser(request):
    user = User('1111', 'zhangsan')
    user.save()
    return HttpResponse(request)


def selectUser(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})