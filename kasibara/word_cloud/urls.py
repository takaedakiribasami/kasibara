from django.urls import path

from .models import Lyric
from . import views

app_name = "word_cloud"
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('add-lyric', views.AddLyricView.as_view(), name="add_lyric"),
    path('lyric-detail/<int:pk>/',
         views.lyricDetailView.as_view(), name="lyric_detail"),
]
