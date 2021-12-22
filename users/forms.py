from django import forms


class SendEmailForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Subject'
    }),
                              max_length=100
                              )
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Describe your issue here'
    }))
