from django.shortcuts import render
from .models import Community

def communities_list(req):
    communities = Community.objects.all().order_by('-date')
    return render(req, 'communities/communities_list.html', {'communities': communities})
# Create your views here.
def Community_page(request, slug):
    community = Community.objects.get(slug=slug)
    return render(request, 'communities/Community_page.html', {'Community': community})