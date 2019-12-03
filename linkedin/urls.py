from django.conf.urls import url
from .views import LinkedinApi

urlpatterns = [
    url(r'^api/$', LinkedinApi.as_view(), name='api')
]
