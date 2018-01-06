from  django import forms




class UserForm(forms.Form):
    name = forms.CharField(label="prenom",max_length=255)
    surname=forms.CharField(label="nom",max_length=255)
    email = forms.EmailField(label="adresse email",max_length=255)
    password= forms.CharField(label="mot de passe",widget=forms.PasswordInput)
    telephone=forms.RegexField(label="numero de téléphone",regex=r'^\+?1?\d{9,15}$')


