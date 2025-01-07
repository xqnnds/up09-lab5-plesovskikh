from django.shortcuts import render, redirect
from .models import Community
from . import forms
from django.contrib.auth.decorators import login_required

def communities_list(req):
    communities = Community.objects.all().order_by('-date')
    return render(req, 'communities/communities_list.html', {'communities': communities})
# Create your views here.
def Community_page(request, slug):
    community = Community.objects.get(slug=slug)
    return render(request, 'communities/Community_page.html', {'Community': community})

@login_required(login_url="/users/login/")
def communities_new(request):
    if request.method == 'POST': 
        form = forms.CreateCommunitie(request.POST, request.FILES) 
        if form.is_valid():
            newpost = form.save(commit=False) 
            newpost.save()
            return redirect('communities:list')
    else:
        form = forms.CreateCommunitie()
    return render(request, 'communities/communitie_new.html', { 'form': form })