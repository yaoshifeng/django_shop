# -*- coding = utf-8
from django.db import models


class UserInfo(models.Model):
    # 用户名
    uname = models.CharField(max_length=20)
    # 密码
    upwd = models.CharField(max_length=10)
    # 邮箱
    uemail = models.CharField(max_length=30)
    # 收货人
    utaker = models.CharField(max_length=20, default='')
    # 邮寄地址
    uaddress = models.CharField(max_length=100, default='')
    # 邮编
    uzipcode = models.CharField(max_length=6, default='')
    # 电话
    uphone = models.CharField(max_length=11, default='')
