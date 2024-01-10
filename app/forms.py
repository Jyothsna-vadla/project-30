from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
        labels={'topic_name':'TN'}
class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name','email']
        exclude=['url']
        labels={'topic_name':'TN'}
class AccessRecordForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'
        #fields=['name','author']
        exclude=['author']
        labels={'name':'N'}