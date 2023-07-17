from django.urls import path, include
from hlo.views import *
from hlo import views
urlpatterns = [
    path("", views.xyzz),
    path("show-this-page", views.showthispage),
    path("abc", views.akjsdka),

    path("conatct", views.contactus),
    path("conatct-us-data", views.getdata),
]
