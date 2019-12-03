from django.conf.urls import url
from .views import LinkedinApi
from django.urls import path, include

urlpatterns = [
    path('auth/callback/', LinkedinApi.as_view(), name='api')
]
