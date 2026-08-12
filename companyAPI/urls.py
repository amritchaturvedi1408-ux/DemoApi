
from django.contrib import admin
from django.urls import include, path

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", views.home_page, name="home"),
    path("api/v1/", include('api.urls')),
    path(
        "api/",
        include("accounts.urls")
    ),
]
