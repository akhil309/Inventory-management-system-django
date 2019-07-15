from django.urls import path

from . import views


app_name = 'Inventory'
urlpatterns = [

    path('', views.index, name = 'index'),

    path('<int:item_id>/',views.detail, name = 'details'),
    path('<int:item_id>/transfer',views.transferitem,name = 'transferitem'),
    path('<int:item_id>/return',views.returnitem,name = 'returnitem'),
]