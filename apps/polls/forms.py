# forms.py
from django import forms
from .models import Poll

class PollForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title",
                "class": "form-control",
            }
        )
    )
    question = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Question",
                "class": "form-control",
            }
        )
    )
    choice1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Choice1",
                "class": "form-control",
            }
        )
    )
    choice2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Choice2",
                "class": "form-control",
            }
        )
    )
    choice3 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Choice3",
                "class": "form-control",
            }
        )
    )
    choice4 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Choice4",
                "class": "form-control",
            }
        )
    )
    deadline = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control",
                "type": "datetime-local",
            }
        )
    )
    
    class Meta:
        model = Poll
        fields = ['title','question', 'choice1','choice2','choice3','choice4','deadline']




