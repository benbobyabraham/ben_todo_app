from django import forms

class todo_form(forms.Form):
    desc = forms.CharField(max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Add todo',
            'autofocus': '',
        })
    )
