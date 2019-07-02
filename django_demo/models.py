# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db.models import Model


# 模型管理器
class UserManager(models.Manager):
    def get_queryset(self):
        return super(UserManager, self).get_queryset().filter(data_status=True)

    def create(self, name, age):
        user = User()
        user.name = name
        user.age = age
        return user


# 用户模型
class User(Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(db_column="age")
    data_status = models.BooleanField(default=True)
    user_manager = UserManager()

    # @classmethod
    # def create(cls, name, age):
    #     user = User()
    #     user.name = name
    #     user.age = age
    #     return user

    class Meta:
        db_table = "t_user"
        ordering = ["-age"]


class Role(Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User)

    class Meta:
        db_table = "t_role"
