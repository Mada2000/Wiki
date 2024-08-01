from django.shortcuts import render
from django.http import Http404
from django.shortcuts import redirect
import random
from . import util

def index(request):
    # Check if method is POST
    if request.method == "POST":
        #get the data from the form 
        title = request.POST.get('title')
        content = request.POST.get('content')

        #if title or content is empty
        if not content or not title:
            return render(request, "encyclopedia/404.html", {
                "error": "please put a Title and content."
            })
        #if title name is existing 
        elif title.title() in util.list_entries() or title in util.list_entries():
            return render(request, "encyclopedia/404.html", {
                "error": "Title is already in use."
            })
        
        #if title name isn't existing before
        else:
            util.save_entry(title, content)
            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries()
            })
    # if no form is submitted
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })
    
def search(request):
    entries = []
    if request.GET['q']:
        query = request.GET['q']

        #iterate over all the entries
        for entry in util.list_entries():

            # check if the query is found
            # redirect user to the page if found
            if query.lower() == entry.lower():
                return render(request, f"encyclopedia/content.html", {
                    "name":entry , "entry":util.get_entry(entry)
                })
            
            # add to the list the titles that has the query in it
            elif query.lower() in entry.lower():
                entries.append(entry)

        # list all the entries that have the query in their title 
        if entries:
            return render(request, "encyclopedia/index.html", {
                "entries": entries
            })
        
        return render(request, "encyclopedia/404.html")

    return render(request, "encyclopedia/404.html")
    
def new(request):
    return render(request, "encyclopedia/new.html")


#in case of any random route in the url 
def unkown(request, name):
    if request.method == "POST":
        #get the data from the form 
        title = request.POST.get('title')
        content = request.POST.get('content')
        if not content or not title:
            return render(request, "encyclopedia/404.html", {
                "error": "Please put content."
            })
        else:
            util.save_entry(title, content)
            return render(request, "encyclopedia/content.html", {
                "name":title , "entry":util.get_entry(title)
            })
    else:
        #if the route is there redirect user to the page content
        for entry in util.list_entries():

            # redirect user to the page if found
            if name.lower() == entry.lower():
                return render(request, f"encyclopedia/content.html", {
                    "name":entry , "entry":util.get_entry(entry)
                })

        
        #if not display an error page
        else:
            return render(request, "encyclopedia/404.html")


def edit(request):
    if request.method == "POST":
        title = request.POST.get('title')
        return render (request, "encyclopedia/edit.html",{
            "title":title
        })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })
    
def random_page(request):
    #create empty list for the entries and append them
    entries = []
    for entry in util.list_entries():
        entries.append(entry)

    #get random title from list and view it
    random_title = random.choice(entries)
    return render(request, f"encyclopedia/content.html", {
        "name":random_title , "entry":util.get_entry(random_title)
    })