from django.urls import path
from products import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetails.as_view(), name='product'),
    path('', views.ProductList.as_view(), name='product-list'),
]