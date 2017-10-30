from django import forms
#from .models import User

class Userform(forms.Form):
	#CHAT = forms.CharField(max_length=500)
    CHAT = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2, 'cols': 70}))
	#chat = forms.CharField(widget=forms.Textarea)
    #chat =forms.Textarea
