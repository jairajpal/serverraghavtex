# myapp/urls/product.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views.product import ProductViewSet
from myapp.views.product import ProductUploadView

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls), name='product'),  # This should work as expected
    path('upload/', ProductUploadView.as_view(), name='product-upload'),
]
