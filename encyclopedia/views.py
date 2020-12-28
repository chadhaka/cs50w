from django.shortcuts import render

from . import util
from markdown2 import Markdown
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    entryMD = util.get_entry(entry)
    md = Markdown()
    if entryMD != None:
       entryHtml = md.convert(entryMD)
    #    print(entryHtml)
       return render(request, "encyclopedia/entry.html", {
           "title": entry.capitalize(),
           "bodyText": entryHtml 
           })
    return render(request, "encyclopedia/error.html")

def search(request):
    class NewTaskForm(forms.Form):
        searchform = forms.CharField(label="Search Encyclopedia")
    # if request.method == "POST":
    #     searchForm = NewTaskForm(request.POST) 
    #     if searchForm.is_valid():
    #         query = searchForm.cleaned_data["query"]
    #         return render(request, "encyclopedia/test.html", {
    #             "query": query
    #         })
    #         # print(query)
    #         entryCheck = util.get_entry(query)
    #         print(entryCheck)
    #         if entryCheck != None:
    #             return entry(request, query)
    #         else:
    #             entriesList = util.list_entries()
    #             results = list(filter(lambda x: query in x, entriesList)) 
    #             queryTitle = "Showing results for: " + query
    #             return render(request, "encyclopedia/searchresults.html", {
    #                 "title": queryTitle,
    #                 "resultsFound": results >= 1,
    #                 "results": results
    #             })
    #     else:
    #         return render(request, "encyclopedia/index.html", {
    #             "searchform": query
    #         })

            #return HttpResponseRedirect(reverse("encyclopedia:index"))
    return render(request, "encyclopedia/index.html", {
        "searchform": NewTaskForm()
    })



