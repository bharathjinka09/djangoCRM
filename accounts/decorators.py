from django.http import HttpResponse
from django.shortcuts import redirect, render

'''
A decorator will take another function as a parameter
and adds functionality to it (Here view_func is the function from
views.py as a parameter and modifies the functionality of that view)
'''


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
            # return render(request,'accounts/unauthenticated_user.html')

    return wrapper_func


# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_funct(request, *args, **kwargs):

#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name
#                 if group in allowed_roles:
#                     # return view_func(request, *args, **kwargs)
#                     return render(request,'accounts/dashboard.html')
#             else:
#                 # return HttpResponse('You are not authorized to view this page!')
#             	return render(request,'accounts/unauthenticated_user.html')
        		
#         return wrapper_funct
#     return decorator


# def admin_only(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():
#             group = request.user.groups.all()[0].name

#         if group == 'customer':
#             return redirect('user-page')

#         if group == 'admin':
#             return view_func(request, *args, **kwargs)

#     return wrapper_func
