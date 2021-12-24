from django import forms
from .models import Lyric


class AddLyricForm(forms.ModelForm):
    class Meta:
        model = Lyric
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control mx-5 my-2"
