"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from api import views

urlpatterns = [
    
    url('getstate', views.get_device_status),
    url('state_list', views.DeviceStatusList.as_view()),
    
    url('getconfig', views.get_config),
    url('add_edit_config', views.AddEditConfig.as_view()),
    url('delete_config', views.DeleteConfig.as_view()),
    url('admin/', admin.site.urls),
    url('/', views.DeviceList.as_view()),
    url('', views.DeviceList.as_view()),
]
