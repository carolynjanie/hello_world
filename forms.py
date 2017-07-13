from django import forms
class commentPostForm(forms.form)
    name=forms.charfield(max_length=50)
    email=forms.charfield(max_length=50)
    to=forms.charfield(max_length=50)
    comment=forms.charfield(required=False,widget=forms.Textarea)
