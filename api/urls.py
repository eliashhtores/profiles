from django.urls import path
from .views import HelloApiView

urlpatterns = [
    path('hello-api/', HelloApiView.as_view(), name='hello-api'),
]
