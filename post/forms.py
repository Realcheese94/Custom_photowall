from django import forms
from .models import Comment


class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'content',
        )
        widgets = {
            'content':forms.TextInput(
                attrs={
                    'class' : 'content',
                    'placeholder':'comment...',
                }
            )
        }
    def clean_content(self):
        data = self.cleaned_data['content']
        errors = []
        if data == '':
            errors.append(forms.ValidationError('please insert your reply'))
        elif len(data) > 10:
            errors.append(forms.ValidationError('please less reply'))
        if errors:
            raise forms.ValidationError(errors)
        return data
   


