from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name':'Home Shop',
        'name': 'I Made Surya Anahata Putra',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
