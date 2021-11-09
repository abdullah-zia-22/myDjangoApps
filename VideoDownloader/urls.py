from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#dynamic patterns
app_name = 'VideoDownloader'
urlpatterns = [
    path("", views.index,name="index"),
    path("downloadinsta",views.downloadinsta),
    path("downloadFb",views.downloadFb,name="downloadFb")

    
]
urlpatterns+=staticfiles_urlpatterns()