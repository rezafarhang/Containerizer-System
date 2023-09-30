"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from containerizer.views import AppViewSet, RunningHistoryView, RunContainerView,RunNewContainerView, StopContainerView


app_name = 'containerizer'

app_router = routers.DefaultRouter()
app_router.register('', AppViewSet, basename='App')


urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('app/', include(app_router.urls)),
    path('app/<int:app_id>/run', RunNewContainerView.as_view(), name='run_app_view'),

    path('container/<str:container_id>/run/', RunContainerView.as_view(), name='run_container_view'),
    path('container/<str:container_id>/stop/', StopContainerView.as_view(), name='stop_view'),

    path('history/', RunningHistoryView.as_view(), name='history_view'),


]
