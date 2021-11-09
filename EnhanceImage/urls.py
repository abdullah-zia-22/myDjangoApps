from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#dynamic patterns
app_name = 'EnhanceImage'
urlpatterns = [
    path("", views.index,name="index"),
    path("SuperRes",views.SuperRes),
    path("waifu",views.waifu),
    path("toonify",views.toonify)

]
urlpatterns+=staticfiles_urlpatterns()