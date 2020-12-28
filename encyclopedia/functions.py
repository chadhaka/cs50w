from django.shortcuts import render
from . import util, forms
from markdown2 import Markdown
from django.urls import reverse
from django.http import HttpResponseRedirect

def entryConvert(entry):
    entryMD = util.get_entry(entry)
    md = Markdown()
    if entryMD != None:
       entryHtml = md.convert(entryMD)
       return True, entryHtml
    else:
        return False, ""

def searchDirect(query):
    entryCheck = util.get_entry(query)
    
    if entryCheck != None:
        return HttpResponseRedirect(reverse("encyclopedia:entry", kwargs={
            "entry": query
            }))
    else:
        return HttpResponseRedirect(reverse("encyclopedia:search", kwargs={
            "query": query
            }))
        

def searchResults(query):
    entriesList = util.list_entries()
    results = list(filter(lambda x: query.lower() in x.lower(), entriesList)) 
    queryTitle = "Showing results for: " + query
    return len(results)>0, queryTitle, results

def searchForm(request):
    # Post method - search query is submitted
    if request.method == "POST":
        searchForm = forms.SearchForm(request.POST)
        if searchForm.is_valid():
            query = searchForm.cleaned_data["query"]
            return searchDirect(query)
        else:
            # form is invalid, re-render each page with searchform / existing information displayed
            return searchForm

    # Get method - search form is created
    return forms.SearchForm()
    