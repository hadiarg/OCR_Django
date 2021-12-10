from django.http import  HttpRequest, request
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user_is_authenticated:
            return redirect('dashboard')
        else:
            return  view_func(request, *args, **kwargs)
    return wrapper_func

def auuneticated_user(allowed_role=[]):
    def decorator(view_func):
        def  wrapper_func(request, *args, **kwargs):
            gorup = None
            if request.user.group.exist():
                group = request.user.group.all()[0].name
            
            if group in allowed_role:
                return view_func(request, *args, **kwargs)
            else:
                return HttpRequest('You are not Authorized to voew this page')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_function(requset, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            froup = request.user.group.all()[0].name
        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function