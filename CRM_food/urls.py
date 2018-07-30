from django.contrib import admin
from django.conf.urls import url, include
from CRM import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include('CRM.urls')),
]

