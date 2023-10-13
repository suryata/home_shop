from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('logout/', logout_user, name='logout'),
    path('tambah/<int:id>/', tambah_amount, name='tambah_amount'),
    path('kurang/<int:id>/', kurang_amount, name='kurang_amount'),
    path('hapus/<int:id>/', hapus_item, name='hapus_item'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete-ajax/<int:id>/',delete_item_ajax,name='delete_item_ajax'),
]