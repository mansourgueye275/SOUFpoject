from  django import forms
from django.core.exceptions import ValidationError


class UserForm(forms.Form):
    name = forms.CharField(label="prenom",max_length=255,required=True)
    surname=forms.CharField(label="nom",max_length=255,required=True)
    email = forms.EmailField(label="adresse email",max_length=255,required=True)
    password= forms.CharField(label="mot de passe",widget=forms.PasswordInput,required=True)
    confirm_password= forms.CharField(label="confirmation de mot de passe",widget=forms.PasswordInput,required=True)
    telephone=forms.RegexField(label="numero de téléphone",regex=r'^\+?1?\d{9,15}$',required=True)

    def clean(self):
        if (self.cleaned_data['password'] !=
                self.cleaned_data['confirm_password']):

            raise ValidationError("Les mots de passe de sont pas identiques.")

        return self.cleaned_data



class SigninForm(forms.Form):
    email= forms.EmailField(label="email",max_length=255,required= True)
    password= forms.CharField(label="mot de passe",help_text='entrez votre mot de passe',widget=forms.PasswordInput,required=True)
