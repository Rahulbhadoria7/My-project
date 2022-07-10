from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    records={}
    url="https://inshorts.deta.dev/news?category="
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['indexdata1']=inshorts_data
    return render(request,'index.html',records)

def business(request):
    records={}
    url="https://inshorts.deta.dev/news?category=business"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['businessdata2']=inshorts_data
    return render(request,'business.html',records)

def entertainment(request):
    records={}
    url="https://inshorts.deta.dev/news?category=entertainment"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['entertainmentdata3']=inshorts_data
    return render(request,'entertainment.html',records)

def politics(request):
    records={}
    url="https://inshorts.deta.dev/news?category=politics"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['politicdata4']=inshorts_data
    return render(request,'politics.html',records)

def sports(request):
    records={}
    url="https://inshorts.deta.dev/news?category=sports"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['sportsdata5']=inshorts_data
    return render(request,'sports.html',records)

def nationalnews(request):
    records={}
    url="https://inshorts.deta.dev/news?category=national"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['nationalnewsdata6']=inshorts_data
    return render(request,'nationalnews.html',records)

def startup(request):
    records={}
    url="https://inshorts.deta.dev/news?category=startup"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['startupdata7']=inshorts_data
    return render(request,'startup.html',records)

def technology(request):
    records={}
    url="https://inshorts.deta.dev/news?category=technology"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['technologydata8']=inshorts_data
    return render(request,'technology.html',records)

def world(request):
    records={}
    url="https://inshorts.deta.dev/news?category=world"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['worlddata9']=inshorts_data
    return render(request,'world.html',records)

def miscellaneous(request):
    records={}
    url="https://inshorts.deta.dev/news?category=miscellaneous"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['miscellaneousdata10']=inshorts_data
    return render(request,'miscellaneous.html',records)

def hatke(request):
    records={}
    url="https://inshorts.deta.dev/news?category=hatke"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['hatkedata11']=inshorts_data
    return render(request,'hatke.html',records)

def science(request):
    records={}
    url="https://inshorts.deta.dev/news?category=science"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['sciencedata12']=inshorts_data
    return render(request,'science.html',records)

def Automobile(request):
    records={}
    url="https://inshorts.deta.dev/news?category=automobile"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['Automobiledata13']=inshorts_data
    return render(request,'Automobile.html',records)