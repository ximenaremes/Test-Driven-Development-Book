"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.conf.urls import include, url
# from lists import views as list_views  
# from lists import urls as list_urls  

# from django.contrib import admin

from django.conf.urls import url
from lists import views

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]

# urlpatterns = [
#     url(r'^$', views.home_page, name='home'),
# ]

# urlpatterns = [
#     url(r'^$', views.home_page, name='home'),
#     url(r'^lists/the-only-list-in-the-world/$', views.view_list, name='view_list'),
# ]
# urlpatterns = [
#     url(r'^$', views.home_page, name='home'),
#     url(r'^lists/new$', views.new_list, name='new_list'),
#     url(r'^lists/the-only-list-in-the-world/$', views.view_list, name='view_list'),
# ]
# urlpatterns = [
#     url(r'^$', list_views.home_page, name='home'),
#     url(r'^lists/', include(list_urls)),  
# ]
urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),
]