from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("account/", include("django.contrib.auth.urls")),
    path("logout/", views.logmeout, name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("messagex/list", views.getmymessages, name="messagex_list"),
    #path("dbdump/", views.downloaddb, name="dbdump"),
    #path("dbdump/", views.downloadmessages, name="dbdump"),
    path("dbdump/", views.downloadtest, name="dbdump"),
    path("messagex/create", views.MessagexCreate.as_view(), name="messagex_create"),
]
