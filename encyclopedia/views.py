from django import forms
from django.shortcuts import render
from . import util, functions
from markdown2 import Markdown
from django.urls import reverse
from django.http import HttpResponseRedirect



def index(request):
    if request.method == "GET":
        searchform = functions.searchForm(request)
    else:
        return functions.searchForm(request)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "searchform": searchform
    })

def entry(request, entry):
    if request.method == "GET":
        searchform = functions.searchForm(request)
        entryResult, entryHtml = functions.entryConvert(entry)
        if entryResult:
            return render(request, "encyclopedia/entry.html", {
                "title": entry.capitalize(),
                "bodyText": entryHtml,
                "searchform": searchform 
                })
        else:
            return render(request, "encyclopedia/error.html", {
                "searchform": searchform,
                "error": "Error! Page not found"
                })
    else:

        return functions.searchForm(request)

def search(request, query):
    
    if request.method == "GET":
        searchform = functions.searchForm(request)
    



def newpage(request):
    if request.method == "GET":
        searchform = functions.searchForm(request)
        pageform = functions.newPage(request)
        return render(request, "encyclopedia/newpage.html", {
        "searchform": searchform,
        "pageform": pageform
        })
    else:
        try:
            return functions.newPage(request)
        except:
            request.method = "GET"
            searchform = functions.searchForm(request)
            return render(request, "encyclopedia/error.html", {
            "searchform": searchform,
            "error": "Error! Page Already Exists"
            })

def random(request):
    entry = functions.randomEntry()
    return HttpResponseRedirect(reverse("encyclopedia:entry", kwargs={
            "entry": entry
            }))






