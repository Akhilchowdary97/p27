from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
# Create your views here.
def create_topic(request):
    if request.method=="POST":
        topic=request.POST.get("topic")
        t=Topic.objects.get_or_create(topic_name=topic)
        if t[1]==True:
            t[0].save()
            return HttpResponse("<h2>Topic Added Successfully</h2>")
        else:
            return HttpResponse("<h2>Topic Is Already Exist In Table</h2>")
    return render(request,"create_topic.html")

def create_webpage(request):
    if request.method=="POST":
        topic=request.POST.get('topic')
        name=request.POST.get('name')
        url=request.POST.get("url")
        t=Topic.objects.get_or_create(topic_name=topic)[0]
        w=Webpage.objects.get_or_create(topic=t,name=name,url=url)[0]
        w.save()
        return HttpResponse("<h2>Webpage Added Successfully</h2>")
    topics=Topic.objects.all()
    return render(request,"create_webpage.html",context={'topics':topics})
def display_topics(request):
    topics=Topic.objects.all()
    return render(request,"display_topic.html",context={'topics':topics})
def display_webpages(request):
    webpages=Webpage.objects.all()
    return render(request,"display_webpage.html",context={'webpages':webpages})
def display_topic(request,id):
    topics=Topic.objects.filter(id=id)
    return render(request,"display_topic.html",context={'topics':topics})
def display_webpage(request,id):
    webpages=Webpage.objects.filter(id=id)
    return render(request,"display_webpage.html",context={'webpages':webpages})