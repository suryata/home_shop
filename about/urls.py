from django.urls import path
from about.views import show_about

app_name = 'about'

urlpatterns = [
    path('', show_about, name='show_about'), 
]