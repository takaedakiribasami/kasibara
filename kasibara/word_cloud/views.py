from django.urls.base import reverse, reverse_lazy
from django.views import generic
from .forms import AddLyricForm
from .models import Lyric
from .models import get_word_cloud
from django.shortcuts import render


class IndexView(generic.ListView):
    model = Lyric
    template_name = "index.html"


class AddLyricView(generic.CreateView):
    model = Lyric
    template_name = "add_lyric.html"
    form_class = AddLyricForm
    success_url = reverse_lazy("word_cloud:index")


class lyricDetailView(generic.DetailView):
    model = Lyric
    template_name = 'lyric_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        target = Lyric.objects.filter(pk=self.kwargs['pk']).first()
        context['wc_img_base64'] = get_word_cloud(target.content)
        return context
