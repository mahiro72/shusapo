from .models import Company,SAnalysis,ES,IAnalysis
from django import forms


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name','comment')


class SAnalysisForm(forms.ModelForm):
    class Meta:
        model = SAnalysis
        fields = ('title','comment')

class ESForm(forms.ModelForm):
    class Meta:
        model = ES
        fields = ('name','date')

class IAnalysisForm(forms.ModelForm):
    class Meta:
        model = IAnalysis
        fields = ('title','comment')