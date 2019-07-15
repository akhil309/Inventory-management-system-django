from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Transaction, Client
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.models import User

# Create your views here.

@login_required
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
        'User': User,
    }
    return render(request, 'Inventory/index.html', context)

@login_required
def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    clients = Client.objects.all()

    return render(request, 'Inventory/details.html', {'item': item, 'clients': clients})

@login_required
def transferitem(request, item_id):
    client = Client.objects.get(place=request.POST.get("client"))
    item=Item.objects.get(pk=item_id)
    quantity=request.POST.get("quantity")

    transaction=Transaction(quantity=quantity, item=item,client=client)
    transaction.save()
    item.quantity=item.quantity-int(quantity)
    item.save()
    return render(request,'Inventory/transferitem.html',{'transaction':transaction,'quantity':quantity,'item':item,'client':client})

@login_required
def returnitem(request,item_id):
    client=Client.objects.get(place=request.POST.get("client"))
    item=Item.objects.get(pk=item_id)
    quantity=request.POST.get("quantity")

    transaction=Transaction(quantity=quantity, item=item,client=client)
    transaction.save()
    item.quantity=item.quantity+int(quantity)
    item.save()
    return render(request,'Inventory/returnitem.html',{'transaction':transaction,'quantity':quantity,'item':item,'client':client})

