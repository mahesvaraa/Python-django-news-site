from django import forms
from .models import News
from django.core.exceptions import ValidationError
from django.utils.html import linebreaks

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='e-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control', "placeholder": "name@example.com"})
    )

    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'})
    )


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'photo', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(
                attrs={"class": "form-switch form-check-input", "type": "checkbox", "role": "switch"})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'сука' in title.lower():
            raise ValidationError('не матюкайся')
        return title
