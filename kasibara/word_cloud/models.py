from django.db import models
from wordcloud import WordCloud
import spacy
import io
import base64
from PIL import Image

FONT_PATH = "/usr/share/fonts/opentype/ipaexfont-gothic/ipaexg.ttf"


class Lyric(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=150)
    released_at = models.DateTimeField(verbose_name="発表年", null=True)
    lyricist = models.CharField(verbose_name="作詞", max_length=100, null=True)
    composer = models.CharField(verbose_name="作曲", max_length=100, null=True)
    singer = models.CharField(verbose_name="歌手", max_length=100, null=True)
    content = models.TextField(verbose_name="本文", null=True)
    word_cloud_img = models.ImageField(verbose_name="ワードクラウド", null=True)

    class Meta:
        verbose_name_plural = "Lyric"

    def __str__(self):
        return self.title


def get_word_cloud(text):
    nlp = spacy.load('ja_ginza')
    doc = nlp(text)

    noun_toks = []
    for tok in doc:
        noun_toks.append(tok)
    wc = WordCloud(font_path=FONT_PATH,
                   max_font_size=40).generate(" ".join(map(lambda tok: tok.text, noun_toks)))

    buffer = io.BytesIO()
    image_array = wc.to_array()
    img = Image.fromarray(image_array)
    img.save(buffer, format="PNG")
    base64Img = base64.b64encode(
        buffer.getvalue()).decode().replace("'", "")

    return base64Img
