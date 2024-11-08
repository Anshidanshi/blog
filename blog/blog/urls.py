"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from home import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('blog.urls')),
    path('', views.post_list, name='post_list'),
    path('post/<id>', views.post_view, name='post_view'),
    path('delete/<id>', views.delete, name='delete'),
    path('post_comments/<int:post_id>/', views.post_comments, name='post_comments'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



        