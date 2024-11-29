from django.shortcuts import render

def posts_list(req):
    return render(req, 'posts/posts_list.html')
# Create your views here.
