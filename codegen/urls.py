from django.contrib import admin
from django.urls import path
from generator import views as v

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", v.home, name="home"),
    path("password/", v.password, name="pass"),
    path("about/", v.about, name="about"),
]
