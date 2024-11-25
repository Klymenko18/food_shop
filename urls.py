from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Адмін панель
    path('', include('Products.urls')),  # Включення URL з додатку Products
]
