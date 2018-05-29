#coding=utf-8
from django.http import HttpResponseRedirect


#如果登录则转到登录页面
def islogin(func):
    def login_fun(request, *args, **kwargs):
        if request.session.get('user_id'):
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login')
            red.set_cookie('url', request.get_full_path)

            # request.get_full_path() - - 获取当前url, (包含参数)
            # 请求一个http: // 127.0.0.1:8000/200/?type=10
            # request.get_full_path()
            # 返回的是【/200/?type=10】
            return red
    return login_fun