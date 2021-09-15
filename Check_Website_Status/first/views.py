from django.http import HttpResponse
from django.shortcuts import render
from .models import websiteurl, FilesUpload
import urllib
import pandas as pd
import csv

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
    # except urllib.error.HTTPError as e:
    #     # Return code error (e.g. 404, 501, ...)
    #     return HttpResponse('NOTWORKING = {}'.format(e.code))

    # except urllib.error.URLError as e:
    #     # Not an HTTP-specific error (e.g. connection refused)
    #     return HttpResponse('URL Error NOTWORKING {}'.format(e.code))
    except:
        website_url = websiteurl(web_name=web, status='not-working')
        website_url.save()
        return HttpResponse('NOTWORKING')


def upload(request):
    if request.method == 'GET':
        return render(request, 'first/template1.html')
    if request.method == "POST":
        file2 = request.FILES["upload1"]
        df = pd.read_csv(file2)
        dic={}
        for i in df.iloc[:,0]:
            try:
                status = urllib.request.urlopen(i).getcode()
                dic[i]="WORKING"
            except:
                dic[i]="NOT-WORKING"
        return render(request, 'first/template1.html',{'dic':dic})
    return render(request, 'first/template1.html')
