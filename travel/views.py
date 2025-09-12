from ast import And
from operator import sub
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
import requests
from .forms import RegistrationForm,bookingform,RegisterHotel,Room,Package
from  travel. models import comment
import datetime

def registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect('login')
    context={'form':form }
    return render(request,'registration.html',context)

def login_user(request):
    try:
      _email=request.GET.get("Email")
      pas=request.GET.get("password")
      print(_email)
      print(pas)
      userdata=Registration.objects.get(email=_email)
      if(userdata.password==pas):
        request.session['user']=userdata.id  
        print("login sucessful")
        return HttpResponseRedirect('/travel/home')
      else:
        print("Login Failed")  
    except:
      print("login failed due to email")  
    return render(request,'login.html')
    
def home(request):
    login=False
    try:
        if( request.session['user']=='' or request.session['user'] == None ):
            pass
        else:  
            login=True      
    except:
         pass
    Data=comment.objects.all()
    Cities=city.objects.all()
    context={'Data':Data,'login':login,'home':'active','list_of_cities':Cities}
    if request.method == 'POST':
        PostData=request.POST.copy()
        _city=city.objects.get(id=PostData['city'])
        list_of_trips=package.objects.filter(price__lte=PostData['amount'],hotel_name__city_name=_city)
        if len(list_of_trips)==0:
            message=f"No trips available in this price range for {_city}"
            context['message']=message
        else:
            context['list_of_trips']=list_of_trips
    return render(request,"home.html",context)

def destination(request):
    login=False
    try:
        if( request.session['user']=='' or request.session['user'] == None ):
            pass
        else:  
            login=True      
    except:
         pass
    all=request.GET.get('q')
    cities=city.objects.all()
    context={'dest':cities,'login':login,'destination':'active'}
    return render(request,"destination.html",context) 
    

def place(request):
    login=False
    try:
        if( request.session['user']=='' or request.session['user'] == None ):
            pass
        else:  
            login=True      
    except:
         pass
    all=request.GET.get('r')
    _id=request.GET.get('q')
    _stID=city.objects.get(id=_id)
    p_data=places.objects.filter(city_name=_stID)
    h_data=hotel.objects.filter(city_name=_stID)
    r_data=restaurant.objects.filter(city_name=_stID)
    storecity=_stID.name
    appid='e8897638844880ef6457b15236dc25a2'
    URL ="https://api.openweathermap.org/data/2.5/weather"
    PARAMS= {'q': storecity , 'appid':appid, 'units': 'metric'}
    temp_city=''
    weather_desc=''
    icon=''
    try:
        api_link = requests.get(url=URL, params=PARAMS)
        api_data = api_link.json()
        if api_data['cod']=='404':
            print ("invalid city")
        else:
            temp_city = ((api_data['main']['temp']) )
            weather_desc =api_data['weather'][0]['description']
            icon=api_data['weather'][0]['icon']  
    except :
        print("Can't get weather from api")
    context={'c_data': _stID  ,'data': p_data , 'hotel_data':h_data , 'destination':'active','login':login,'rest_data':r_data,"t_data":temp_city,"w_data":weather_desc, "icon":icon,"storecity":storecity}
    return render(request,"place.html",context)
    

def rooms(request):
    login=False
    try:
        if( request.session['user']=='' or request.session['user'] == None ):
            pass
        else:  
            login=True      
    except:
         pass
    all=request.GET.get('s')
    _id=request.GET.get('r')
    s_ID=hotel.objects.get(id=_id)
    data=room.objects.filter(hotel_name=s_ID)
    pack=package.objects.filter(hotel_name=s_ID)
    context={'room_data': data,'pack':pack,'h_data':s_ID,'login':login,'destination':'active' }
    return render(request,"rooms.html",context) 

def roombooking(request):
    try:
        if( request.session['user']=='' or request.session['user'] == None ):
            return HttpResponseRedirect('/travel/login')
        else:  
            login=True
    except:
        pass 
    login=False
    try:
        if( request.session['user']=='' or request.session['user'] == None ):
            pass
        else:  
            login=True      
    except:
         pass 
    Error_message=''
    _id=request.GET.get('s')
    s_ID=room.objects.get(id=_id)
    form = bookingform()
    if request.method == "POST":
        form = bookingform(request.POST)
        postData=request.POST.copy()
        check_in=postData['check_in'].split('-')
        check_out=postData['check_out'].split('-')
        today = datetime.datetime.now()
        in_date=datetime.datetime(int(check_in[0]),int(check_in[1]),int(check_in[2]))
        out_date=datetime.datetime(int(check_out[0]),int(check_out[1]),int(check_out[2]))
        if(in_date<today):
            print('OK')
            Error_message='Check_In date is already past'
        elif(out_date<today):
            print('OK')
            Error_message='Check_Out date is already past'
        elif form.is_valid():
            form.instance.hotel_name=s_ID.hotel_name
            form.save()  
            return HttpResponseRedirect('confirm')
    context={'form':form ,'data':s_ID,'login':login,'destination':'active','Error':Error_message}
    return render(request,"roombooking.html",context) 

def packagebooking(request):
    login=False
    try:
        if( request.session['user']=='' or request.session['user'] == None ):
            pass
        else:  
            login=True      
    except:
         pass
    _id=request.GET.get('s')
    s_ID=package.objects.get(id=_id)
    form = bookingform()
    if request.method == "POST":
        form = bookingform(request.POST)
        print(form)
        if form.is_valid():
            form.instance.hotel_name=s_ID.hotel_name
            form.save()  
            return HttpResponseRedirect('confirm')
    context={'form':form ,'data':s_ID,'login':login}
    return render(request,"packagebook.html",context)

def contact(request):
    login=False
    try:
        if( request.session['user']=='' or request.session['user'] == None ):
            pass
        else:  
            login=True      
    except:
         pass
    context={'login':login,'contact':'active'}
    return render(request,"contact.html",context)

def currency(request):
    login=False
    try:
        if( request.session['user']=='' or request.session['user'] == None ):
            pass
        else:  
            login=True      
    except:
         pass
    context={'login':login,'currency':'active'}
    return render(request,"currency.html",context)

def confirm(request):
    return render(request,"confirm.html")

def logout(request):
    request.session['user']=''
    request.session['hotle']=''
    return HttpResponseRedirect('/travel/login')

def reviews(request):
    if request.method == 'POST':
        print(request.POST)
        db=comment()
        db.cus_name=request.POST['firstname']
        db.text=request.POST['comment']
        db.save()
        return HttpResponseRedirect('/travel/home')
    login=False
    try:
        if( request.session['user']=='' or request.session['user'] == None ):
            pass
        else:  
            login=True      
    except:
         pass
    context={'login':login,'destination':'active'}
    return render(request,'review.html',context)
    

def hotel_register(request):
   form =RegisterHotel()
   if request.method == "POST":
        form = RegisterHotel(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = request.user
            image.save() 
            return HttpResponseRedirect('login_hotel')
   context={'form':form }
   return render(request,'hotel_register.html',context)

def login_hotel(request):
    try:
      print('Login Hotel')
      _name=request.GET.get("name")
      pas=request.GET.get("password")
      hoteldata=hotel.objects.get(name=_name)
      if(hoteldata.password==pas):
        request.session['hotle']=hoteldata.id
        print("login sucessful")
        return HttpResponseRedirect('/travel/hotel_site')
      else:
        print("Login Failed")  
    except:
      print("login failed due to email")  
    return render(request,'login_hotel.html')

def hotel_site(request):
    if request.method=='POST':
        postData=request.POST.copy()
        try:
            _room=room.objects.get(id=postData['id'])
            _room.delete()
        except:
            _pkg=package.objects.get(id=postData['pkg_id'])
            _pkg.delete()
    try:
        if( request.session['hotle']=='' or request.session['hotle'] == None ):
            return HttpResponseRedirect('/travel/login_hotel')
        else:    
            hname=request.session['hotle']
            h_data=hotel.objects.get(id=hname)
            data=room.objects.filter(hotel_name=h_data)
            pack=package.objects.filter(hotel_name=h_data)
            context={'h_name':h_data,'room_data': data,'pack':pack } 
    except:
         return HttpResponseRedirect('/travel/login_hotel')
    return render(request,"hotel_site.html",context)            

def add_room(request):
    hname=request.session['hotle']
    h_data=hotel.objects.get(id=hname)
    form =Room()
    if request.method == "POST":
        form = Room(request.POST,request.FILES)
        if form.is_valid():
            form.instance.hotel_name=h_data
            image = form.save(commit=False)
            image.author = request.user
            image.save() 
            return HttpResponseRedirect('hotel_site')
    context={'form':form }
    return render(request,"add_room.html",context)

def add_package(request):
    hname=request.session['hotle']
    h_data=hotel.objects.get(id=hname)
    form =Package()
    if request.method == "POST":
        form = Package(request.POST,request.FILES)
        if form.is_valid():
            form.instance.hotel_name=h_data
            image = form.save(commit=False)
            image.author = request.user
            image.save() 
            return HttpResponseRedirect('hotel_site')
    context={'form':form }
    return render(request,"add_package.html",context)    

def bookings(request):
    hname=request.session['hotle']
    h_data=hotel.objects.get(id=hname)
    data=booking.objects.filter(hotel_name=h_data)
    context={'data':data,'h_name':h_data}
    return render(request,"bookings.html",context)    

def bookings_user(request):
    if request.method=='POST':
        postData=request.POST.copy()
        _booking_id=postData['booking_id']
        _booking=booking.objects.get(id=_booking_id)
        _booking.delete()
    login=False
    try:
        if( request.session['user']=='' or request.session['user'] == None ):
            pass
        else:  
            login=True      
    except:
         pass
    uname=request.session['user']
    u_data=Registration.objects.get(id=uname)
    data=booking.objects.filter(username=u_data.username)
    context={'data':data,'h_name':u_data,'login':login,'booking':'active'}
    return render(request,"bookings_users.html",context) 

def TestPage(request):
    context={'name':'Omer'}
    return render(request,"test.html",context)