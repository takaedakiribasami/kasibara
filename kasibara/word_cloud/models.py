from django.db import models


class Lyric(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=150)
    released_at = models.DateTimeField(verbose_name="発表年", null=True)
    lyricist = models.CharField(verbose_name="作詞", max_length=100, null=True)
    composer = models.CharField(verbose_name="作曲", max_length=100, null=True)
    singer = models.CharField(verbose_name="歌手", max_length=100, null=True)
    content = models.TextField(verbose_name="本文", null=True)

    class Meta:
        verbose_name_plural = "Lyric"

    def __str__(self):
        return self.title
