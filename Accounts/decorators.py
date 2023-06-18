from django.contrib.auth import decorators
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import resolve, reverse
from django.http import HttpResponse

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def super_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser==True:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Something Wrong')
        else:
            return HttpResponse('Something Wrong')
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            # group = None
            if request.user.groups.exists():
                allgroups = request.user.groups.all()
                allowedgroups = []
                for x in allgroups:
                    allowedgroups.append(x.name)

                for y in allowed_roles:
                    if y in allowedgroups:
                        return view_func(request, *args, **kwargs)
                else:
                    # return HttpResponse('You are not authorized to view this page')
                    return render(request,'Accounts/error.html',{'title':'Error'})
                # group = request.user.groups.all()[0].name
                # if group in allowed_roles:
                #     return view_func(request, *args, **kwargs)
                # else:
                #     return HttpResponse('You are not authorized to view this page')
            else:
                # return HttpResponse('You are not authorized to view this page')
                return render(request,'Accounts/error.html',{'title':'Error'})
        return wrapper_func
    return decorator

# ['admin', 'SN ANE', 'SN Ane Mgt', 'SN Ane Pat', 'SN Ane Zon', 'AEex']
def group_review(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            # print(request.user.groups.all()[0].name)
            # if len(request.user.groups.all())>1:
            #     return view_func(request, *args, **kwargs)
            allgroups = request.user.groups.all()
            # print(allgroups)
            # group = request.user.groups.all()[0].name
            
            allowedgroups=[]
            for x in allgroups:
                allowedgroups.append(x.name)
            if 'admin' in allowedgroups:
                return view_func(request, *args, **kwargs)
            elif 'SN ANE' in allowedgroups or 'SN Ane Mgt' in allowedgroups:
                return redirect(reverse('AccidentEmergency:management')+request.session.get('anetype', ''))
            elif 'AEex' in allowedgroups:
                return redirect(reverse('AccidentEmergency:patientList')+request.session.get('anetype', ''))
            elif 'SN Ane Zon' in allowedgroups:
                return redirect(reverse('AccidentEmergency:zone')+request.session.get('anetype', ''))
            elif 'SN Dis Pat' in allowedgroups:
                return redirect(reverse('AccidentEmergency:patient')+request.session.get('anetype', ''))
            elif 'SN Radiology' in allowedgroups:
                return redirect('Radiology:management')
            else:
                return HttpResponse('Something Wrong: ')
        else:
            # return HttpResponse('You are not authorized to view this page')
            return render(request,'Accounts/error.html',{'title':'Error'})
            
    return wrapper_func

# leading to infinite redirect
def check_ane_type(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.exists():
            allgroups = request.user.groups.all().values_list('name', flat=True)
            url_info = resolve(request.path_info)
            app_name = url_info.app_name
            url_name = url_info.url_name
            url = app_name+':'+url_name
            if (request.GET.get('type', '')=='ped' and 'SN Ane Ped' in allgroups) or \
                (request.GET.get('type', '')=='adult' and 'SN Ane Adult' in allgroups):
                return view_func(request, *args, **kwargs)
            else:
                if app_name=='AccidentEmergency':
                    if 'SN Ane Ped' in allgroups:
                        return redirect(reverse(url)+'?type=ped', permanent=True)
                    elif 'SN Ane Adult' in allgroups:
                        return redirect(reverse(url)+'?type=adult', permanent=True)
                    else:
                        return view_func(request, *args, **kwargs)
                else:
                    return view_func(request, *args, **kwargs)
        else:
            return render(request,'Accounts/error.html',{'title':'Error'})
    return wrapper_func
