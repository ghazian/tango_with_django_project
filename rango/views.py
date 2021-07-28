from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # category_list = Category.objects.order_by('name')[:5]
    # context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context=context_dict)
