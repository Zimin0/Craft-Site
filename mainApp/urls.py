from django.urls import path
from mainApp import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('add_product/', views.add_product_view, name='add_product'),
    path('search/', views.search_products, name='search_products'),
    path('delete-product/<int:product_id>/', views.delete_product_view, name='delete_product'),
    path('add-quantity/<int:product_id>/', views.add_quantity_view, name='add_quantity'),
]
