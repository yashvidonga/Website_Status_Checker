from django.http import HttpResponse
from django.shortcuts import render
from .models import websiteurl
import urllib


def home(request):
    return render(request, 'first/template1.html')


def check(request):
    web = request.GET.get('url', 'default')
    if 'https://' not in web:
        web = 'https://'+web
    try:
        status = urllib.request.urlopen(web).getcode()
        website_url = websiteurl(web_name=web, status='working')
        website_url.save()
        return HttpResponse('WORKING')
    except:
        website_url = websiteurl(web_name=web, status='not-working')
        website_url.save()
        return HttpResponse('NOTWORKING')
