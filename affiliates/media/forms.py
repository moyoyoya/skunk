from django import forms

class UserDeeplink(forms.ModelForm):
    link = forms.URLField(label='add your link in here', widget=URLInput)

    def getDeeplink(self):
        if link.