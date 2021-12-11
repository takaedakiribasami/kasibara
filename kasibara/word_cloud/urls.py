from django.urls import path
from . import views

app_name = "word_cloud"
urlpatterns = [
    path('', views.IndexView.as_view(), name="index")
]
