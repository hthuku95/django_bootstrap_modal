from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'',views.frontend, name="frontend"),
    path(r'backend/',views.backend,name="backend"),
    path(r'login/',views.login,name="login"),
    path(r'login_user/',views.LoginUser,name="login_user"),
    path(r'logout_user/',views.LogoutUser,name="loguot_user"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)