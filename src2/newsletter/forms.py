from django import forms
from .models import SignUp
class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email','full_name']
        
        
    def clean_email(self):
        email= self.cleaned_data.get('email')
        email_base,provider=email.split("@")
        domain,extension=provider.split(".")
        #if not domain =='USR':
            #raise forms.ValidationError('please ensure proper domain name')
        if not extension == 'edu':
            raise forms.ValidationError('please enter EDU email addresses')
        return email   
        
    def clean_full_name(self):
        name=self.cleaned_data.get('full_name')
        return name        
