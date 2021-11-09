import os
from django.shortcuts import render
import re
from django.http.response import JsonResponse
import json
import http.cookiejar as cookielib
import requests
import instaloader
from instaloader.exceptions import BadResponseException
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup

def index(request):
    return render(request, 'VideoDownloader.html',{'fblink':'', 'instalink':''})

def downloadinsta(request):
        if request.method=="POST":
            try:
                link=request.POST.get('link')
                username=request.POST.get('username')
                password=request.POST.get('password')
                L = instaloader.Instaloader()
                L.login(username, password)    
                print("login complete")
                if(link.find('reel')!=-1):
                    link=link.replace("https://www.instagram.com/reel/","")
                    link = link.split('/', 1)[0]
                    print(link)
                    post = instaloader.Post.from_shortcode(L.context, link).video_url
                    return JsonResponse(json.dumps({'instalink': post}), safe=False)
                else:
                    link=link.replace("https://www.instagram.com/p/","")
                    link = link.split('/', 1)[0]
                    print(link)
                    post = instaloader.Post.from_shortcode(L.context, link).url
                    return JsonResponse(json.dumps({'instalink': post}), safe=False)
                
            except BadResponseException:
                return JsonResponse(json.dumps({'error': 'Invalid Link','instalink': ''}), safe=False)


def downloadFb(request):
    
    if request.method=="POST":
        link=request.POST.get('link')
        try:
            
            link=link.replace("https://www","")
            link="https://mbasic"+link
            path=  os.path.join(os.path.dirname(os.path.realpath(__file__)), 'facebook.com_cookies.txt')
          
            cj = cookielib.MozillaCookieJar(path)
            cj.load()
          
            html=requests.get(link,cookies=cj).content.decode('utf-8')
            s=BeautifulSoup(html,'html.parser')
            l=s.find('a', {'href': re.compile(r'/video_redirect/')})
            url=l['href']
            url="https://mbasic.facebook.com"+url
            print(url)
            return JsonResponse(json.dumps({'fblink': url}), safe=False)
        except ConnectionError:
            return JsonResponse(json.dumps({'error': 'Invalid Link','fblink': ''}), safe=False)
        