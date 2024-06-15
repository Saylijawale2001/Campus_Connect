"""cjits URL Configuration

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
from django.urls import path,include
from django.contrib.auth import views as auth_views
from testapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login,name='login'),
    path('',views.home,name='home'),
    path('learn/',views.learn,name="learn"),
    path('events/',views.events,name='events'),
    path('documents_list/',views.document_list,name='document_list'),
    path('chat/',views.chat,name='chat'),
    path('notification/',views.notification,name='notification'),
    path('<str:room>/',views.room,name='room'),
    path('chat/checkview', views.checkview, name='checkview'),
    path('send',views.send,name='send'),
    path('logout/',views.logout,name='logout'),
    path('social-auth/',include('social_django.urls',namespace='social')),
    path('getMessages/<str:room>/',views.getMessages,name='getMessages'),   
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)