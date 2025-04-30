from django.urls import path
from products import views

urlpatterns = [
    path('', views.CategoryList.as_view(), name='categores-list'),
    path('<int:pk>/', views.CategoryDetails.as_view(), name='view-specific-category')
]