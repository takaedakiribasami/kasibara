from django import forms
from .models import Lyric
import datetime

today = datetime.date.today()


class AddLyricForm(forms.ModelForm):
    released_at = forms.DateTimeField(
        label='発表年',
        input_formats=['%Y'],
        widget=forms.DateInput(
            format='%Y',
            attrs={'placeholder': 'YYYY'}))

    class Meta:
        model = Lyric
        fields = ('__all__')
        exclude = ('word_cloud_img',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control mx-5 my-2"
