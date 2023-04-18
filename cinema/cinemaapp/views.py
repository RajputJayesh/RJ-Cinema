from django.shortcuts import render,redirect
from django.http import HttpResponse
from cinemaapp.models import Post
import datetime 

# Create your views here.

def reuse(request):
    return render(request,'base.html')

def dashboard(request):
    return render(request,'dashboard.html')

def abc(request):

    return render(request,'abc.html')

def about(request):
    return HttpResponse("Hello jayesh") 

def index(request):

    return render(request,'index.html')

def buy_tickets(request):
    if request.method=="POST":
        n=request.POST['name']
        mob=request.POST['mobile_num']
        show=request.POST['show_time']
        scat=request.POST['seat_cat']
        sseat=request.POST['seat_num']
        

        p=Post.objects.create(name=n,mobile_num=mob,show_time=show,seat_cat=scat,seat_num=sseat,created_on=datetime.datetime.now())
        p.save()

        return render(request,'index.html')


    else:
        return render(request,'buy_tickets.html')

def booked(request):

    p=Post.objects.all()
    content={}
    content['data']=p

    return render(request,'booked.html',content)

def delete(request,rid):

    p=Post.objects.get(id=rid)
    p.delete()
    return redirect('/booked')

def search(request):


    if request.method=="POST":
        
        mob=request.POST['mobile_num']
               
        p=Post.objects.filter(mobile_num=mob)
        content={}
        content['data']=p

        return redirect('/booked')


    else:
        return render(request,'buy_tickets.html')

def home(request):
    return render(request,'index.html')