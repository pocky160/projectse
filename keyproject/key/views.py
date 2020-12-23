from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Booking, Act, Building

# Create your views here.

def Homepage(request):
    return render(request, 'key/home.html')

def Booking(request):
    if request.method == 'POST':
        data = request.POST.copy()
        booking = data.get('booking_name')
        activity = data.get('act_name')
        people = data.get('people')
        timestart = data.get('starttime')
        timestop = data.get('stoptime')
        date = data.get('datebook')
        build = data.get('build')

        newBooking = Booking()
        newBooking.NameBooking = booking
        newBooking.People = people
        newBooking.DateBook = date
        newBooking.TimeStart = timestart
        newBooking.TimeStop = timestop
        newBooking.IDAct = activity
        newBooking.IDBuilding = build
        newBooking.save()

        return redirect('home-page')

    #querry data
    dataAct = Act.objects.all()
    dataBuild = Building.objects.all()
    return render(request, 'key/booking.html', {'Act':dataAct, 'Build':dataBuild})

def History(request):
    # dataBooking = Booking.objects.all()
    # return render(request, 'key/history.html', {'Book':dataBooking})
    return render(request, 'key/history.html')

def Notification(request):
    return render(request, 'key/notification.html')