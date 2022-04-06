from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HelloApiViewSet, UserProfileApiViewSet, UserLoginApiView, ProfileFeedItemViewSet

router = DefaultRouter()
router.register('hello-viewset', HelloApiViewSet, basename='hello_viewset')
router.register('profile', UserProfileApiViewSet)
router.register('profile-feed', ProfileFeedItemViewSet,
                basename='profile_feed')


urlpatterns = [
    path('hello-api/', HelloApiView.as_view(), name='hello_api'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('', include(router.urls)),
]
