from django.http import HttpResponse
from django.shortcuts import render
#from .models import websiteurl
import urllib.request 


def home(request):
    return render(request,'first/home copy.html')

def check(request):
    web = request.GET.get('text','default')
    if 'https://' not in web:
        web = 'https://'+web
    status = urllib.request.urlopen(web).getcode()
    #website_url = websiteurl(web_name=web)
    #website_url.save()
    if(status == 200):
        return HttpResponse('WORKING')
    else:
        return HttpResponse('NOTWORKING')