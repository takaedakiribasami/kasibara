# Generated by Django 4.0 on 2021-12-12 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_cloud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lyric',
            name='author',
        ),
        migrations.AddField(
            model_name='lyric',
            name='composer',
            field=models.CharField(max_length=100, null=True, verbose_name='作曲'),
        ),
        migrations.AddField(
            model_name='lyric',
            name='lyricist',
            field=models.CharField(max_length=100, null=True, verbose_name='作詞'),
        ),
        migrations.AddField(
            model_name='lyric',
            name='singer',
            field=models.CharField(max_length=100, null=True, verbose_name='歌手'),
        ),
    ]
