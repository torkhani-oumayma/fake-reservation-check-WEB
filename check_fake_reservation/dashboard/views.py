from django.shortcuts import render
from .decorators import *
from authentication.models import Passenger
from .form import CreatePassengerForm  , CreateUserForm, CreateFlightForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Flight
# Create your views here.


#@unauthenticated_user
def home_admin_reservation_dashboard (request):
    
    context ={
        'segment':'Reservation',
        'dashboard_type':'Reservation dashboard',
        }
    return render(request, 'home/index_reservation.html', context)


#User Controllerss
def user_list (request):
    users = User.objects.all()    
    print(User)
    context ={
        'users' : users,
        'segment':'users',
        'dashboard_type':'List Users',
        }
    return render(request, 'home/users/list.html', context)

def add_user (request):
    #ena lehna ................... 
    form  = CreateUserForm()
    if request.method == 'POST' :
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            
            user = form.save()  
            passenger = Passenger.objects.create(user=user, name= username , first_name = first_name, last_name= last_name, email= email)
            return redirect ('user_list')
        else :
            print (form.errors)
            messages.error(request,"Verif : ",form.errors)
    context ={
        'form':form ,
        'segment':'users',
        'dashboard_type':'Add User',
        }
    return render(request, 'home/users/form.html', context)

def show_user (request, pk):
    user = User.objects.get(id=pk)

    context ={
        'user':user,
        'segment':'users',
        'dashboard_type':'Show Users',
        }
    return render(request, 'home/users/show.html', context)

def delete_user (request,pk):
    user = User.objects.get(id=pk)
    
    if request.method == "POST":
        user.delete()
        return redirect('user_list')
    
    context ={
        'user':user,
        'segment':'users',
        'dashboard_type':'Delete Users',
        }
    return render(request, 'home/users/delete.html', context)

def update_user (request, pk):
    user = User.objects.get(id=pk)
    passenger = Passenger.objects.get (user =user)
    form = CreateUserForm(instance=user)

    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=user)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email'] 
              
            passenger.name = username
            passenger.first_name = first_name
            passenger.last_name = last_name
            passenger.email = email
            passenger.save()   
                    
            new_user = form.save()  

            return redirect('user_list')
        else :
            messages.error(request,"Verif User Passwords: ",form.errors)
        
    context ={
        'user':user,
        'form':form,
        'segment':'users',
        'dashboard_type':'Update Passengers',
        }
    return render(request, 'home/users/update.html', context)
    


#Passenger Controllerss
def passenger_list (request):
    passengers = Passenger.objects.all()    
    context ={
        'passengers' : passengers,
        'segment':'passengers',
        'dashboard_type':'List Passengers',
        }
    return render(request, 'home/passengers/list.html', context)

def add_passenger (request):
    form  = CreatePassengerForm()
    if request.method == 'POST' :
        #print('Printing POST', request.POST)
        form = CreatePassengerForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect ('passenger_list')
    context ={
        'form':form ,
        'segment':'passengers',
        'dashboard_type':'Add passengers',
        }
    return render(request, 'home/passengers/form.html', context)

def show_passenger (request, pk):
    passenger = Passenger.objects.get(id=pk)

    context ={
        'passenger':passenger,
        'segment':'passengers',
        'dashboard_type':'Show Passengers',
        }
    return render(request, 'home/passengers/show.html', context)

def delete_passenger (request,pk):
    passenger = Passenger.objects.get(id=pk)
    user = passenger.user
    if request.method == "POST":
        passenger.delete()
        user.delete()
        return redirect('passenger_list')
    
    context ={
        'passenger':passenger,
        'segment':'passengers',
        'dashboard_type':'Delete Passengers',
        }
    return render(request, 'home/passengers/delete.html', context)

def update_passenger (request,pk):
    passenger = Passenger.objects.get(id=pk)
    form = CreatePassengerForm(instance=passenger)
    
    if request.method == 'POST':
        form = CreatePassengerForm(request.POST, instance=passenger)
        if form.is_valid():            
            form.save()  
            return redirect('passenger_list')
        else :
            messages.error(request,"Verif Passenger Passwords: ",form.errors)
        
    context ={
        'form':form ,
        'segment':'passengers',
        'dashboard_type':'Update Passengers',
        }
    return render(request, 'home/passengers/update.html', context)
    
#flights Controllerss
def flights_list (request):
    flights = Flight.objects.all()
    
    context ={
        'flights':flights ,
        'segment':'flights',
        'dashboard_type':'List Flights',
        }
    return render(request, 'home/flights/list.html', context)

def add_flight (request):
    form  = CreateFlightForm()
    if request.method == 'POST' :
        form = CreateFlightForm(request.POST)
        if form.is_valid():
            instance = form.save()  
            instance.flight_duration = (instance.flight_end - instance.flight_start).total_seconds() //3600
            instance.save()

            return redirect ('flight_list')
        else:
            print("------------", form.errors)
            messages.error(request, form.errors)
    context ={
        'form':form ,
        'segment':'flights',
        'dashboard_type':'Add Flight',
        }
    return render(request, 'home/flights/form.html', context)

def show_flight (request, pk):
    flight = Flight.objects.get(id=pk)

    context ={
        'flight': flight,
        'segment':'flights',
        'dashboard_type':'Show flights',
        }
    return render(request, 'home/flights/show.html', context)

def delete_flight (request,pk):
    flight = Flight.objects.get(id=pk)
    
    if request.method == "POST":
        flight.delete()
        return redirect('flight_list')
    
    context ={
        'flight':flight,
        'segment':'flight',
        'dashboard_type':'Delete Flight',
        }
    return render(request, 'home/flights/delete.html', context)

def update_flight (request,pk):
    flight = Flight.objects.get(id=pk)
    form = CreateFlightForm(instance=flight)
    
    if request.method == 'POST':
        form = CreateFlightForm(request.POST, instance=flight)
        if form.is_valid():            
            instance = form.save()  
            instance.duration = (instance.flight_start - instance.flight_end).total_seconds() //3600
            instance.save()
            return redirect('flight_list')
                
    context ={
        'flight':flight,
        'form':form ,
        'segment':'flight',
        'dashboard_type':'Update Flight',
        }
    return render(request, 'home/flights/update.html', context)


#flights available Controllerss
def flights_available_list (request):
    flights = Flight.objects.filter(available=True)
    
    context ={
        'flights':flights ,
        'segment':'flights_available',
        'dashboard_type':'List Flights available',
        }
    return render(request, 'home/flights_available/list.html', context)




#predict_reservation
def predict_reservation_list (request):
    context ={
        'segment':'predict_reservations',
        'dashboard_type':'List Reservations predicted',
        }
    return render(request, 'home/predict_reservation/list.html', context)


def reservation_list (request):
    context ={
        'segment':'reservations',
        'dashboard_type':'List Reservations',
        }
    return render(request, 'home/reservation/list.html', context)

def predict_reservation_list (request):
    context ={
        'segment':'predict_reservations',
        'dashboard_type':'List Reservations predicted',
        }
    return render(request, 'home/predict_reservation/list.html', context)


def my_reservation_list (request):
    context ={
        'segment':'my_reservations',
        'dashboard_type':'List of my reservations',
        }
    return render(request, 'home/my_reservation/list.html', context)


def user_profil (request):
    user = request.user
    form = CreateUserForm(instance=user)  
    if user.is_staff == True:
        will_update_pass = False
    else:
        will_update_pass = True
        passenger = Passenger.objects.get(user = user ) 
        
    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=user)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            
            if will_update_pass == True :
                passenger.name = username
                passenger.first_name = first_name
                passenger.last_name = last_name
                passenger.email = email
                passenger.save()   
                       
            user = form.save()  

            return redirect('login')
        else :
            messages.error(request,"Verif User Passwords")
        
    context ={
        'user':user,
        'form':form,
        'segment':'profil',
        'dashboard_type':'My Profil',
        }
    return render(request, 'home/profile.html', context)
    