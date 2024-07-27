from django.shortcuts import render
from django.http import Http404
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound 
from django.http import HttpResponse



from . import util

#if request.method == "GET":
        #query = request.GET("q")
        #return render(request, "encyclopedia/index.html", {
         #   "entries": util.get_entry(query)
        #})

def index(request):
    
    return render(request, "encyclopedia/index.html", {
         "entries": util.list_entries()
    })
    
def search(request):
    if request.method == "GET":
        query = request.GET['q']
        if query in util.list_entries():
            return render(request, "encyclopedia/search.html", {
                "entries": query
            })
        #return render(request, "encyclopedia/search.html")
    else:
        return render(request, "encyclopedia/django.html")
    

def css(request):
    return render(request, "encyclopedia/css.html")

def django(request):
    return render(request, "encyclopedia/django.html")

def git(request):
    return render(request, "encyclopedia/git.html")

def html(request):
    return render(request, "encyclopedia/html.html")

def py(request):
    return render(request, "encyclopedia/py.html")



