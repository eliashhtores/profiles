from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HelloApiViewSet, UserProfileApiViewSet

router = DefaultRouter()
router.register('hello-viewset', HelloApiViewSet, basename='hello_viewset')
router.register('profile', UserProfileApiViewSet)


urlpatterns = [
    path('hello-api/', HelloApiView.as_view(), name='hello_api'),
    path('', include(router.urls)),
]
