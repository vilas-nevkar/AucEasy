from django import forms
from .models import AdminUser


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = AdminUser
        fields = (
            'admin_name',
            'admin_username',
            'admin_email',
            'admin_password',
            'admin_confirm_password',
        )

        widgets = {
            'admin_password': forms.PasswordInput(),
            'admin_confirm_password': forms.PasswordInput()
        }
        # exclude = (
        #     'admin_contact',
        #     'country',
        #     'state',
        #     'city',
        #     'area',
        # )

    def clean_admin_password(self):
        password = self.cleaned_data.get('admin_password')
        return password


class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control py-4',
            'id': 'inputEmailAddress',
            'placeholder': 'Enter username'}),
    )
    email = forms.EmailField(
        max_length=30,
        widget=forms.EmailInput(attrs={
            'class': 'form-control py-4',
            'id': 'inputEmailAddress',
            'placeholder': 'Enter Email'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control py-4',
            'id': 'inputPassword',
            'placeholder': 'Enter password'
        })
    )
