
from django import forms
from .models import blogModel
from froala_editor.widgets import FroalaEditor


class createBlogForm(forms.ModelForm):
    # blog_content = forms.CharField(widget=FroalaEditor)
    class Meta:
        model=blogModel
        fields=['blogContent']
    
