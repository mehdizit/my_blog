from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="username",widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd = forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control'}))

class RegisterForm(forms.Form):
    username = forms.CharField(label="username",widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd = forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    pwd_confirm = forms.CharField(label="password confirmation",widget=forms.PasswordInput(attrs={'class':'form-control'}))

