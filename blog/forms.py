from django import forms
from .models import Contact, Comment


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, required=True)
    email = forms.EmailField(required=True)
    to = forms.EmailField(required=True)
    comments = forms.CharField(widget=forms.Textarea, required=False)
