from django.forms import ModelForm, Textarea
from MainApp.models import Snippet, Comment


class SnippetForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code']


class CommentForm(ModelForm):
   class Meta:
       model = Comment
       # Описываем поля, которые будем заполнять в форме
       fields = ['text']
       widgets = {
           'text': Textarea(attrs={'rows':2, 'placeholder': 'Комментарий...'})
       }

