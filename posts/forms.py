from django import forms
from django.forms import ModelForm
from .models import Post, Tag


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'state', 'categories', 'tags', 'content', 'image']
        widgets = {
            'categories': forms.CheckboxSelectMultiple,
            'tags': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # self.fields['tags'].widget.attrs.update({'style': "OVERFLOW-Y:scroll;"})
        # self.fields['tags'] = forms.ModelChoiceField(widget=forms.CheckboxSelectMultiple,
        # queryset=Tag.objects.all(), empty_label=None)
