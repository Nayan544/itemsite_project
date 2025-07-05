from django.shortcuts import render,get_object_or_404
from .models import Item
from rest_framework import viewsets
from .serializers import ItemSerializer

# Create your views here.

def item_list(request):
    items = Item.objects.all()[:10]
    return render(request, 'catalog/item_list.html', {'items': items})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'catalog/item_detail.html', {'item': item})


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer