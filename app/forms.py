from django import forms
from . import models

class ThreadForm(forms.ModelForm):
    class Meta:
        model = models.Threat
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ThreadForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f] = forms.CharField(
            widget = forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': f,
                    'maxlength': 140
                }
            )
        )

class TestimonyForm(forms.ModelForm):
    class Meta:
        model = models.Testimony
        exclude = ['threat']
    def __init__(self, *args, **kwargs):
        super(TestimonyForm, self).__init__(*args, **kwargs)
        self.fields['choice'] = forms.TypedChoiceField(
                   choices = (
                        (True, 'True'),
                        (False, 'False')
                       ),
                   widget = forms.RadioSelect(
                       attrs={
                           }
                       ))
        self.fields['comment'] = forms.CharField(
            widget = forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '3',
                    'placeholder': 'Your comment here...'
                    }
            )
        )

class AuthForm(forms.ModelForm):
    class Meta:
        model = models.Testimony
        exclude = ['threat', 'choice']
    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args, **kwargs)
        self.fields['comment'] = forms.CharField(
            widget = forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '3',
                    'placeholder': 'Your comment here...'
                    }
            )
        )

class TopicForm(forms.ModelForm):
    class Meta:
        model = models.Topic
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f] = forms.CharField(
            widget = forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': f,
                    'maxlength': 140
                }
            )
        )
