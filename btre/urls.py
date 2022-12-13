"""btre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static


# urlpatterns is API
# '/' API
# '/' LISTINGS
# /MEDIA/ 不是開放給public用的，是一條路徑，但不是API，與上面3者不在同一範圍內
urlpatterns = [
    # eg: /about or /index or /login, 冇後續嘅會自動歸入 "page"
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    # LISTINGS/ ->go listings/urls.py/
    path('admin/', admin.site.urls)   # /admin 會自動歸入admin
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
