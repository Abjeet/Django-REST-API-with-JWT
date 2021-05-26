from django.shortcuts import render
from django.shortcuts import render, redirect
from user.form_validator import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.http.response import JsonResponse
from django.contrib import messages  # import messages
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:homepage")
        else:
            a={}
            for field, errors in form.errors.items():
                a[field] = ','.join(errors)
            data = {
                'status': 'failed',
                'message': 'Unsuccessful registration. Invalid information.',
                'a':a

            }
            return JsonResponse(data)
    else:
        data = {
            'status': 'failed',
            'message': 'Only POST request allowed.',

        }
        return JsonResponse(data)




