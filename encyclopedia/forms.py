from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label="Search Encyclopedia")

class PageForm(forms.Form):
    title = forms.CharField(label="Enter Title")
    content = forms.CharField(label="Enter Content", widget=forms.Textarea)
    
