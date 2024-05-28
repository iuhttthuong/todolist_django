from django import forms

from .models import Task

class TaskForm (forms.ModelForm):
    content = forms.CharField (label = '', max_length = 100, required=True)
    class Meta:
        model = Task
        fields = ['content']

    