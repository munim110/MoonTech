from django.urls import path
from .views import ProductViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ProductViewSet, basename='products')
router.register('category', CategoryViewSet, basename='categories')


urlpatterns = [
] + router.urls
