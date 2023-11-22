from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.core import serializers
from main.models import Item

user = None

@csrf_exempt
def register(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    if User.objects.filter(username=username).exists():
        return JsonResponse({
            "status": False,
            "message": "Username sudah digunakan. Pilih username lain."
        }, status=400)

    # Buat user baru tanpa menggunakan email
    user = User.objects.create_user(username=username, password=password)

    return JsonResponse({
        "username": user.username,
        "status": True,
        "message": "Registrasi berhasil!"
    }, status=201)


@csrf_exempt
def login(request):
    global user
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)
    
@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
    

def get_item_json(request):
    item = Item.objects.filter(user = user)
    return HttpResponse(serializers.serialize('json', item))