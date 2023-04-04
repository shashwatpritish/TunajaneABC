from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home, name="Home"),
    path("use/",views.use, name="Use"),
    path("contact/",views.contact, name="Contact"),
]