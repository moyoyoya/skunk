from django import forms
from django.contrib.auth.models import User
from .models import Profile, Relation


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don\'t match")
        return cd['password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('company_name', 'address', 'country')
        exclude = ('user',)


class RelationForm(forms.ModelForm):
    class Meta:
        model = Relation
        exclude = ('user',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
