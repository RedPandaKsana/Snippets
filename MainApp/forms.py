from django.forms import ModelForm, Textarea
from MainApp.models import Snippet, Comment
from django.contrib.auth.models import User
from django import forms


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


class UserRegistrationForm(ModelForm):
    password1 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password']
