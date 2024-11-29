from django.shortcuts import render
def communities_list(req):
    return render(req, 'communities/communities_list.html')
# Create your views here.
