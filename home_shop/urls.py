from django.contrib import admin
from django.urls import path, include
from home_shop.views import register, login_user


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('about/',include('about.urls')),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
]
