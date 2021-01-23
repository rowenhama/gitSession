
from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from kasiraiLogin import views

urlpatterns = [
    path('kasiraiLogin/', include('kasiraiLogin.urls')),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
