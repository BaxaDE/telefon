from django import forms


class ContactForms(forms.Form):
    name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder': 'To`liq ismingiz'}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'E-mail'}
        )
    )
    messege = forms.CharField(
        min_length=20,
        widget=forms.Textarea(
            attrs={'placeholder': 'Xabaringiz mazmuni'}
        )
    )
