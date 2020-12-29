from django.shortcuts import render
from . import util, forms
from markdown2 import Markdown
from django.urls import reverse
from django.http import HttpResponseRedirect
from random import randint

def entryCheck(entry):
    entryExists = False
    entryCheck = util.get_entry(entry)
    if entryCheck != None:
        entryExists = True
    return entryExists

def entryConvert(entry):    
    if entryCheck(entry):
        entryMD = util.get_entry(entry)
        md = Markdown()
        entryHtml = md.convert(entryMD)
        return True, entryHtml
    else:
        return False, ""

def searchDirect(query):
    # Returns redirected page to user based on whether entry exists or not
    
    if entryCheck(query):
        return HttpResponseRedirect(reverse("encyclopedia:entry", kwargs={
            "entry": query
            }))
    else:
        return HttpResponseRedirect(reverse("encyclopedia:search", kwargs={
            "query": query
            }))

def searchResults(query):
    # Finds all entries that exist for given query
    entriesList = util.list_entries()
    results = list(filter(lambda x: query.lower() in x.lower(), entriesList)) 
    queryTitle = "Showing results for: " + query
    return len(results)>0, queryTitle, results

def searchForm(request):
    if request.method == "POST":
        # Post method - search query is submitted and form submit happens
        searchForm = forms.SearchForm(request.POST)
        if searchForm.is_valid():
            query = searchForm.cleaned_data["query"]
            return searchDirect(query)
        else:
            # form is invalid, re-render each page with searchform / existing information displayed
            return searchForm
    # Get method - search form is created
    return forms.SearchForm()
    
def newPage(request):
    if request.method == "POST":
        # Post method - new page submission
        pageForm = forms.PageForm(request.POST)
        if pageForm.is_valid():
            title = pageForm.cleaned_data["title"]
            if not entryCheck(title):
                content = pageForm.cleaned_data["content"]
                util.save_entry(title,content)
                return HttpResponseRedirect(reverse("encyclopedia:entry", kwargs={
                    "entry": title
                    }))
            else:
                raise Exception("Page already exists!")
        else:
            # form is invalid, re-render each page with searchform / existing information displayed
            return pageForm
    # Get method - search form is created
    return forms.PageForm()

def randomEntry():
    entriesList = util.list_entries()
    return entriesList[randint(0, len(entriesList)-1)] 
    