# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django_demo.models import User


def index(request):
    # request.GET.get("key")
    # request.GET.getlist("key")
    # request.POST["key"]
    # request.session["session"] = "sessionName"
    # request.session.get("session", "no login")
    # request.clear()
    # request.flush()
    # temp = loader.get_template("django_demo/index.html")
    # return HttpResponse(temp.render())
    params = {"users": User.user_manager.all()}
    return render(request, "django_demo/index.html", params)


def role(request, userId):
    user = User.user_manager.get(pk=userId)
    roles = user.role_set.all()
    params = {"roles": roles}
    return render(request, "django_demo/role.html", params)

def role2(request):
    userId = request.GET.get("userId")
    user = User.user_manager.get(pk=userId)
    roles = user.role_set.all()
    params = {"roles": roles}
    return render(request, "django_demo/role.html", params)
