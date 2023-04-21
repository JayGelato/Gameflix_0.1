"""Gameflix URL Configuration

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
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from Gameflix_app.views import (
    enter_page,
    home_page,
    login_request,
    logout_request,
    register_request,
    account_settings,
    profile,
    gallery_view,
    videos_view,
    upload_view,
    video_item_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', enter_page, name="entrance"),
    path('homepage/', home_page, name="homepage"),
    path('login/', login_request, name="login"),
    path('logout/', logout_request, name="logout"),
    path('register/', register_request, name="register"),
    path('account_update/', account_settings, name='account_update'),
    path('profile/', profile, name='profile'),
    path('gallery/', gallery_view, name='gallery'),
    path('videos/', videos_view, name='videos'),
    path('upload/', upload_view, name='upload'),
    path('video/<int:video_id>/', video_item_view, name='video_item')
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)