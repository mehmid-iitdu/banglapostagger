from .models import Sentences
from django import forms
from django.forms import ModelForm
from .models import Sentence_Tag

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Sentences
        fields = ['sentence']
        widgets = {
            'sentence': forms.TextInput(
                attrs={'class': "form-control", 'placeholder': "sentence", 'type': "text"}),
        }


class PostForm(forms.ModelForm):

    class Meta:
        model = Sentence_Tag
        fields = ('sentence', 'tag','word')