from django.http import HttpResponse
from django.shortcuts import render
from .models import websiteurl, FilesUpload
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


def upload(request):
    if request.method == 'GET':
        return render(request, 'first/template1.html')
    if request.method == "POST":
        file2 = request.FILES["upload1"]
        document = FilesUpload.objects.create(file=file2)
        document.save()
        return HttpResponse("File Uploaded")
    return render(request, 'first/template1.html')
