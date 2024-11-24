from django.urls import path
from . import views

urlpatterns = [
    path('', views.look_all_products, name='index'),  # Головна сторінка з усіма продуктами
    path('product/<int:id>/', views.product_detail, name='product_detail'),  # Сторінка деталів продукту
]
