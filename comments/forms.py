from django.forms import ModelForm
from django import forms

from comments.models import Comment

# Create the form class.
class CommentForm(ModelForm):
    name = forms.CharField(max_length=10, 
        error_messages={ 'max_length': 'Less than 10 character.'})
    class Meta:
        model = Comment