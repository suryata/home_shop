from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    products = Item.objects.filter(user=request.user)
    total_item = 0
    for i in products:
        total_item += 1
    context = {
        'app_name':'Home Shop',
        'name': request.user.username,
        'class': 'PBP A',
        'products': products,
        'total_item': total_item,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('index'))
    response.delete_cookie('last_login')
    return response

def tambah_amount(request, id):
    if request.method == "POST":
        item = Item.objects.get(pk=id)
        item.amount += 1
        item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def kurang_amount(request, id):
    if request.method == "POST":
        item = Item.objects.get(pk=id)
        if item.amount > 0:
            item.amount -= 1
            item.save()
        if item.amount == 0:
            item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def hapus_item(request, id):
    if request.method == "POST":
        item = Item.objects.get(pk=id)
        item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))