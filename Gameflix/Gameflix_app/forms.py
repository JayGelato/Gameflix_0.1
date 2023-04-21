from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User, Video, Comments


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'username',
                                                                       'class': 'input'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'password',
                                                                           'id': 'myInput',
                                                                           'class': 'input'}))


class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'username', 'class': 'input'}))
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'email', 'class': 'input'}))
    first_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'name', 'class': 'input'}))
    last_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'surname', 'class': 'input'}))
    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder': 'password', 'id': 'myInput', 'class': 'input'}))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder': 'confirm password', 'class': 'input'}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=True)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class AccountSettingsForm(forms.ModelForm):
    username = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'username', 'class': 'input'}))
    email = forms.EmailField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'email', 'class': 'input'}))
    first_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'name', 'class': 'input'}))
    last_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'surname', 'class': 'input'}))
    password1 = forms.CharField(required=False, label="", widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'input'}))
    password2 = forms.CharField(required=False, label="", widget=forms.PasswordInput(attrs={'placeholder': 'confirm password', 'class': 'input'}))
    image = forms.ImageField(required=False, label="Choose your avatar", widget=forms.FileInput(attrs={'class': 'btn'}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2", 'image')


class UploadForm(forms.ModelForm):
    title = forms.CharField(required=False, label="Title: ", widget=forms.TextInput(attrs={'placeholder': 'Set video title', 'class': 'input'}))
    video = forms.FileField(required=False, label="File: ", widget=forms.FileInput(attrs={'placeholder': 'Select video file', 'class': 'input'}))

    class Meta:
        model = Video
        fields = ['title', 'video']

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = False

class CommentForm(forms.ModelForm):
    content = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Write your comments...', 'class': 'input'}))

    class Meta:
        model = Comments
        fields = ['content']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.video = kwargs.pop('video', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.user = self.user
        comment.video = self.video
        if commit:
            comment.save()
        return comment
