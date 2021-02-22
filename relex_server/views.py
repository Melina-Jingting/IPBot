from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from .utils import *
import json



def upload_resume(request):
        return render(request,'upload.html')

def dashboard(request):
    context={}
    if request.method == "POST":
        profile = str(request.FILES["filename"]).split('.')[0]
        request.session['profile']=profile
    context["tree_json"] = create_career_map_json(request.session.get('profile'))
    return render(request,'dashboard.html',context)


def linkedin(request):
    return render(request,'registration/linkedin.html')