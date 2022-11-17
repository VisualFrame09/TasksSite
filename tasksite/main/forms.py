from .models import Task
from django.forms import ModelForm, widgets, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=["title","task"]
        widgets={
            'title': TextInput(attrs={'class':'form-control','id':'exampleFormControlInput1'}),
            'task': Textarea(attrs={'class': 'form-control','id':'exampleFormControlTextarea1','rows':5 }),
        }