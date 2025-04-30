from django.urls import path,include
from products.views import ProductViewSet, CategoryViewSet, ReviewViewset, ProductImageViewset
from rest_framework_nested import routers
from order.views import CartViewSet,CartItemViewSet, OrderViewset

# product App router
router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename = 'products')
router.register('categories', CategoryViewSet, basename='categories')
product_router = routers.NestedDefaultRouter(
    router,
    'products',
    lookup='product'
)
product_router.register('reviews', ReviewViewset, basename='product-review')
product_router.register('images', ProductImageViewset, basename='product-image')

# order app
router.register('carts', CartViewSet, basename='carts')
router.register('orders', ProductImageViewset, basename='orders')

cart_router = routers.NestedDefaultRouter(
    router,
    'carts',
    lookup='cart'
)
cart_router.register('items', CartItemViewSet, basename='cart-item')
urlpatterns = [
    # product app
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    # order app
    path('', include(cart_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]