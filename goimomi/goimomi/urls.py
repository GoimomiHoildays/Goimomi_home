"""
URL configuration for goimomi project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from goimomiapp import views


urlpatterns = [
    path('', include('goimomiapp.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('customized_holidays/', views.customized_holidays, name='customized_holidays'),
    path('customized_umrah/', views.customized_umrah, name='customized_umrah'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)