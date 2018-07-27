from django.contrib import admin
from django.conf.urls import url, include
from CRM import views
from .views import CreateUserAPIView, UserRetrieveUpdateAPIView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^user/$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^department/$', views.DepartmentList.as_view()),
    url(r'^department/(?P<pk>[0-9]+)/$', views.DepartmentDetail.as_view()),
    url(r'^meal/$', views.MealList.as_view()),
    url(r'^meal/(?P<pk>[0-9]+)/$', views.MealDetail.as_view()),
    url(r'^check/$', views.CheckList.as_view()),
    url(r'^check/(?P<pk>[0-9]+)/$', views.CheckDetail.as_view()),
    url(r'^order/$', views.OrderList.as_view()),
    url(r'^order/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view()),
    url(r'^status/$', views.StatusList.as_view()),
    url(r'^status/(?P<pk>[0-9]+)/$', views.StatusDetail.as_view()),
    url(r'^role/$', views.RoleList.as_view()),
    url(r'^role/(?P<pk>[0-9]+)/$', views.RoleDetail.as_view()),
    url(r'^table/$', views.TableList.as_view()),
    url(r'^table/(?P<pk>[0-9]+)/$', views.TableDetail.as_view()),
    url(r'^category/$', views.CategoryList.as_view()),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^create/$', CreateUserAPIView.as_view()),
    url(r'^obtain_token/',obtain_jwt_token),
    url(r'^update/$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls')),
]

