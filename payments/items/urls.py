from django.urls import path

from . import views


app_name = 'items'

urlpatterns = [
    path('buy/<int:item_id>/', views.buy, name='buy'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
]
