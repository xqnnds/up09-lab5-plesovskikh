from django.shortcuts import render
def about(req):
    return render(req, "about.html")

def index(req):
    return render(req, "index.html")
    