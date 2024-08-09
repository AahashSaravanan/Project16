from django import forms
from app.models import *

class Topicdf(forms.Form):
    topic_name = forms.CharField(max_length=100)

class Webpagedf(forms.Form):
    topic_name= forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(max_length=100)
    url=forms.URLField()
'''
class AccessRecorddf(forms.Form):
    name = forms.ModelChoiceField()
    author= forms.CharField(max_length=100)
    date = forms.DateField()'''

class TopicModelForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'

class WebpageModelForm(forms.ModelForm):
    class Meta():
        model=Webpage
        #fields='__all__'
        exclude=['url']


class AccessrecordsModelForm(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields='__all__'
        #exclude=['author']
