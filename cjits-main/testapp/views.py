from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from requests import post
from testapp.models import Room,Message,Document,Video,Links,Notify
from django.http import HttpResponse,JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

#Login View
def login(request):
    return render(request,'login.html')

@login_required
def home(request):
    return render(request,'home.html')

@login_required
def chat(request):
    return render(request,'chat.html')
@login_required
def logout(request):
    return render(request,'login.html')

@csrf_exempt
def room(request, room):
    username=request.GET.get('username')
    if Room.objects.filter(name=room).exists():
        room_details=Room.objects.get(name=room)
        return render(request,'room.html',{
        'username':username,
        'room':room,
        'room_details':room_details
        })
    else:
        return render(request,'login.html')    
    

@csrf_exempt
def checkview(request):
    room=request.POST['room_name']
    username=request.POST['username']
    
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
    
@csrf_exempt
def send(request):
    message=request.POST['message']
    username=request.POST['username']
    room_id=request.POST['room_id']
    
    new_message=Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('message send successfully')


def getMessages(request,room):
    room_details=Room.objects.get(name=room)
    Messages=Message.objects.filter(room=room_details.id)
    
    return JsonResponse({"messages":list(Messages.values())})

@login_required
def learn(request):
    links=Links.objects.all()
    return render(request,'learn.html',{'links':links})

@csrf_exempt
def events(request):
    time=datetime.now()
    videos=Video.objects.all()
    return render(request,'events.html',{'videos':videos,'time':time})
@csrf_exempt
def document_list(request):
    documents=Document.objects.all()
    return render(request,'document_list.html',{'documents':documents})

@csrf_exempt
def notification(request):
    time=datetime.now()
    notification=Notify.objects.all()
    return render(request,'notification.html',{'notification':notification,'time':time})
