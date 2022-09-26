from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("account/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("logout/", views.logmeout, name="logout"),
    path("messagex/inbots", views.getmyinbots, name="messagex_inbots"),
    path("messagex/sent", views.getmysent, name="messagex_sent"),
    path("messagex/create", views.MessagexCreate.as_view(), name="messagex_create"),
    path("dbdump/", views.downloaddb, name="dbdump"),
]
