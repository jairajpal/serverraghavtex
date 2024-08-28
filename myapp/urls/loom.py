# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..views.loom import LoomViewSet
from ..views.loom import LoomUploadView

router = DefaultRouter()
router.register(r'looms', LoomViewSet)

urlpatterns = [
    path('looms/upload/', LoomUploadView.as_view(), name='loom-upload'),
    path('', include(router.urls), name="loom"),

]
