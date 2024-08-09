from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from app.forms import *

# Create your views here.

def insert_topic(request):
    if request.method == 'POST':
        topic_name= request.POST['topic']
        TO = Topic.objects.get_or_create(topic_name=topic_name)[0].save()
        #return HttpResponse("Topic is Added")
        topic_retrive = Topic.objects.all()
        dretrive = {'topics' : topic_retrive }
        return render (request,'retrievetopic.html',dretrive)
    
    return render (request,'topichtml.html')


def insert_webpage(request):
    if request.method == 'POST':
        tn = request.POST['topic']
        name= request.POST['name']
        url= request.POST['url']
        topic_name= Topic.objects.get(topic_name = tn )
        WO = Webpage.objects.get_or_create( topic_name=topic_name,name = name,url = url)[0].save()  
        #return HttpResponse("Webpage object is Added")
        webpage_retrive = Webpage.objects.all()
        dwbretrive = {'wb' : webpage_retrive }
        return render (request,'retrievewebpage.html',dwbretrive)       
    TWO = Topic.objects.all()
    d = {'topics': TWO}
    return render (request,'webpagehtml.html',d)


def insert_accessrecords(request):
    if request.method == 'POST':
        name = request.POST['name']
        author= request.POST['author']
        date= request.POST['date']
        namewb= Webpage.objects.get(name = name )
        ARO = AccessRecord.objects.get_or_create( name=namewb,author = author,date = date)[0].save()  
        #return HttpResponse("Access Record is Added")
        accessrecord_retrive = AccessRecord.objects.all()
        arretrive = {'ar' : accessrecord_retrive }
        return render (request,'retrieveaccessrecord.html',arretrive)       
    WARO = Webpage.objects.all()
    d4 = {'names': WARO}
    return render (request,'accessrecord.html',d4)

def select_topic(request):
    if request.method=='POST':
        topics=request.POST.getList('topics')
        webpages=Webpage.objects.none()
        for topicn in topics:
            webpages=webpages|Webpage.objects.filter(topic_name=topicn)
        d1={'webpages': webpages}
        return render(request,'select_topic.html',d1)
    
def update_accessrecord(request):
    AccessRecord.objects.filter(name=2).update(author = 'Harshad Vali')
    accessrecord_retrive = AccessRecord.objects.all()
    arretrive = {'ar' : accessrecord_retrive }
    return render (request,'retrieveaccessrecord.html',arretrive)    

def topic_model_mf(request):
    EMFTO=TopicModelForm()
    d = {'EMFTO' : EMFTO}
    if request.method=='POST':
        TODMF=TopicModelForm(request.POST)
        TODMF.save()
    return render(request,'topicmf.html',d)   

def webpage_model_mf(request):
    EMFWO=WebpageModelForm()
    d = {'EMFWO' : EMFWO}
    if request.method=='POST':
        WODMF=WebpageModelForm(request.POST)
        WODMF.save()
    return render(request,'wpmfhtml.html',d)


def accessrecord_model_mf(request):
    EMFARO=AccessrecordsModelForm()
    d = {'EMFARO' : EMFARO}
    if request.method=='POST':
        WODMF=AccessrecordsModelForm(request.POST)
        WODMF.save()
    return render(request,'Accessrmf.html',d)

def topic_df(request):
    TDFO = Topicdf()
    d={'TDFO': TDFO}
    return render(request,'topicdjf.html',d)


def webpage_df(request):
    WPDFO = Webpagedf()
    d={'WPDFO': WPDFO}
    return render(request,'webpagedjf.html',d)


def accessrecord_df(request):
    ARDFO = AccessRecord.objects.all()
    d={'ARDFO': ARDFO}
    return render(request,'accessrecordsdjf.html',d)

    


