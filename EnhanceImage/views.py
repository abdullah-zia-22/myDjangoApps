from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Image
from .form import ImageForm
import requests
import json



# Create your views here.
def index(request):
    form=ImageForm() 
    return render(request, 'EnhanceImage.html',{'form':form,'result':''})
    

def SuperRes(request):

    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            
        image=Image.objects.first()
        
        image="media/"+str(image.photo)
        r = requests.post(
        "https://api.deepai.org/api/torch-srgan",
        files={
            'image': open(image,'rb')
        },
        headers={'api-key': '160d0ed1-709d-4de2-be35-7b5a62faf9f3'}
        )

        Image.objects.all().delete()
        result=r.json()
        return JsonResponse(json.dumps({'result': result["output_url"]}), safe=False)
        

    else:
        form=ImageForm()
        return render(request, 'EnhanceImage.html',{'form':form, 'result':''})
    

def waifu(request):

        if request.method=="POST":
                form=ImageForm(request.POST,request.FILES)
                if form.is_valid():
                    form.save()
                    
                image=Image.objects.first()
                
                image="media/"+str(image.photo)
                r = requests.post(
                "https://api.deepai.org/api/waifu2x",
                files={
                    'image': open(image,'rb')
                },
                headers={'api-key': '160d0ed1-709d-4de2-be35-7b5a62faf9f3'}
                )

                Image.objects.all().delete()
                result=r.json()
            
                return JsonResponse(json.dumps({'resultw': result["output_url"]}), safe=False)

        else:
            form=ImageForm()
            return render(request, 'EnhanceImage.html',{'form':form, 'resultw':''})
    

def toonify(request):
        if request.method=="POST":
                    form=ImageForm(request.POST,request.FILES)
                    if form.is_valid():
                        form.save()
                        
                    image=Image.objects.first()
                    
                    image="media/"+str(image.photo)
                    r = requests.post(
                        "https://api.deepai.org/api/toonify",
                    files={
                        'image': open(image,'rb')
                    },
                    headers={'api-key': '160d0ed1-709d-4de2-be35-7b5a62faf9f3'}
                    )

                    Image.objects.all().delete()
                    result=r.json()
                
                    return JsonResponse(json.dumps({'resultn': result["output_url"]}), safe=False)

        else:
            form=ImageForm()
            return render(request, 'EnhanceImage.html',{'form':form, 'resultn':''})