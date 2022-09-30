from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'',views.frontend, name="frontend"),
    path(r'',views.backend,name="backend"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)