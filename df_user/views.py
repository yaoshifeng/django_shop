# -*- coding = utf-8
from django.shortcuts import render, redirect
from df_user.models import UserInfo
from hashlib import sha1


def register(request):
    return render(request, 'df_user/register.html')


# def register_handle(request):
#     post = request.POST
#     uname = post.get('user_name')
#     upwd = post.get('pwd')
#     upwd2 = post.get('cpwd')
#     uemail = post.get('email')
#     # 判断两次密码
#     if upwd != upwd2:
#         return redirect('/user/register')
#     # 密码加密
#     s1 = sha1()
#     s1.update(upwd)
#     upwd3 = s1.hexdigest()
#     # 创建对象
#     user = UserInfo()
#     user.uname = uname
#     user.upwd = upwd3
#     user.uemail = uemail
#     # 存入数据库
#     user.save()
#     # 注册成功后， 转到登录页面
#     return redirect('/user/login/')