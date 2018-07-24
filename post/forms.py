from django import forms


class Commentform(forms.Form):
    content = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class' :'content',
                'placeholder': 'input comment',
            }            
        )
    )
    def clean_content(self):
        data = self.cleaned_data['content']
        errors=[]
        

