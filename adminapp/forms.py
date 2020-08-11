from django import forms
from .models import AdminUser
from productapp.models import ProductCategory, ProductSubcategory


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = AdminUser
        fields = '__all__'
        # exclude = (
        #     'admin_contact',
        #     'country',
        #     'state',
        #     'city',
        #     'area',
        # )
        # fields = (
        #     'admin_name',
        #     'admin_username',
        #     'admin_email',
        #     'admin_password',
        #     'admin_confirm_password',
        # )

        widgets = {
            'admin_password': forms.PasswordInput(),
            'admin_confirm_password': forms.PasswordInput()
        }

    def clean_admin_password(self):
        password = self.cleaned_data.get('admin_password')
        return password


class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control py-4',
            'id': 'inputUsername',
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


class ProductFilterForm(forms.Form):

    date = forms.DateField(widget=forms.SelectDateWidget())
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.values_list('productcategory_name', flat=True))
    subcategory = forms.ModelChoiceField(queryset=ProductSubcategory.objects.values_list('productsubcategory_name', flat=True))
