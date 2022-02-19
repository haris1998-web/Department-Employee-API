from django.urls import re_path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^departments/$', views.departmentAPI),
    re_path(r'^departments/([0-9]+)$', views.departmentAPI),

    re_path(r'^employees/$', views.employeeAPI),
    re_path(r'^employees/([0-9]+)$', views.employeeAPI),

    re_path(r'^employees/SaveFile$', views.saveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)