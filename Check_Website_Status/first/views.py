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
    website_dict = {"website_name": web, "status": "", "code": 200}
    try:
        status = urllib.request.urlopen(web).getcode()
        website_dict["status"] = "Working"
        website_dict["code"] = status
        website_url = websiteurl(web_name=web, status='working', status_code = status)
        website_url.save()
        return render(request,'first/response.html', {'website_dict': website_dict, 'flag': 1})
    except urllib.error.HTTPError as e:
        website_dict["status"] = "Not-Working"
        website_dict["code"] = e.code
        website_url = websiteurl(web_name=web, status='not-working', status_code = e.code)
        website_url.save()
    #     # Return code error (e.g. 404, 501, ...)
        return render(request,'first/response.html', {'website_dict': website_dict, 'flag': 1})

    except urllib.error.URLError as e:
        website_dict["status"] = "Not-Working"
        website_dict["code"] = e.code
        website_url = websiteurl(web_name=web, status='not-working', status_code = e.code)
        website_url.save()
    #     # Not an HTTP-specific error (e.g. connection refused)
        return render(request,'first/response.html', {'website_dict': website_dict, 'flag': 1})
    except:
        website_dict["status"] = "Not-Working"
        website_dict["code"] = status
        website_url = websiteurl(web_name=web, status='not-working', status_code = status)
        website_url.save()
        return render(request,'first/response.html', {'website_dict': website_dict,'flag': 1})


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
                dic[i]="Working"
            except urllib.error.HTTPError as e:
                dic[i]='Not-Working : {}'.format(e.code)
            except urllib.error.URLError as e:
                dic[i]='Not-Working :{}'.format(e.code)
            except:
                dic[i]="Not-Working"
        return render(request, 'first/response.html',{'dic':dic , 'flag': 2})
    return render(request, 'first/response.html')
