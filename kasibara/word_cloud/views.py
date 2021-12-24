from django.urls.base import reverse, reverse_lazy
from django.views import generic
from .forms import AddLyricForm
from .models import Lyric
from django.shortcuts import render


class IndexView(generic.ListView):
    model = Lyric
    template_name = "index.html"


class AddLyricView(generic.CreateView):
    model = Lyric
    template_name = "add_lyric.html"
    form_class = AddLyricForm
    success_url = reverse_lazy("word_cloud:lyric_list")


class lyricDetailView(generic.DeleteView):
    model = Lyric
    template_name = 'lyric_detail.html'
