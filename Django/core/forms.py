from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegisterForm(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text='Enter your full name')
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        help_texts = {
            'username': '',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('name')
        user.email = self.cleaned_data.get('email')
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
            profile_pic = self.cleaned_data.get('profile_picture')
            UserProfile.objects.create(user=user, profile_picture=profile_pic)
        return user
