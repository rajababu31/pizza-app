from django.shortcuts import render
from django.http import HttpResponse
from .models import  pizza

def index(request):
    '''pizzas= pizza.objects.all()
    pizza_names=[ pizza.name  +":" + str(pizza.price) + "$"  for pizza in pizzas ]

    pizza_Str=", ".join(pizza_names)

    return HttpResponse("Our sweet pizza" + pizza_Str) '''
# Create your views here.
    pizzas=pizza.objects.all().order_by('price')
    return render(request, 'menu/index.html',{'pizzas':pizzas})
