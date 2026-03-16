from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from datetime import date
from .models import Profile


class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Usuario",
            "autocomplete": "off"
        })
    )

    first_name = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nombre",
            "autocomplete": "off"
        })
    )

    last_name = forms.CharField(
        label="Apellido",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Apellido",
            "autocomplete": "off"
        })
    )

    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Email",
            "autocomplete": "off"
        })
    )

    birthday = forms.DateField(
        label="Fecha de nacimiento",
        widget=forms.DateInput(attrs={
            "class": "form-control",
            "type": "date"
        })
    )

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "autocomplete": "new-password"
        })
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "autocomplete": "new-password"
        })
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "birthday",
            "password1",
            "password2",
        ]

    def clean_birthday(self):

        birthday = self.cleaned_data.get("birthday")

        today = date.today()

        age = today.year - birthday.year - (
            (today.month, today.day) < (birthday.month, birthday.day)
        )

        if age < 15:
            raise forms.ValidationError(
                "Debes tener al menos 15 años para crear una cuenta."
            )

        return birthday


class CustomLoginForm(AuthenticationForm):

    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Usuario",
            "autocomplete": "off"
        })
    )

    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Contraseña",
            "autocomplete": "new-password"
        })
    )


class EditProfileForm(forms.ModelForm):

    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )

    first_name = forms.CharField(
        label="Nombre",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    last_name = forms.CharField(
        label="Apellido",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["avatar", "bio", "birthday"]

        widgets = {
            "bio": forms.Textarea(attrs={"class": "form-control"}),
            "birthday": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
        }