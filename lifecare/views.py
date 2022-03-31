from django.shortcuts import render,redirect


from lifecare.models import Booking
# Create your views here.

'''def lifecare(request):
    return render(request,'index.html')'''


def booking(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        day = request.POST.get('day')
        date = request.POST.get('date')
        doc = request.POST.get('doc')
        textarea_message = request.POST.get('textarea_message')
        Booking.objects.create(name=name, email=email,day=day,date=date,doc=doc,textarea_message=textarea_message)
        return redirect('lifecare:booking')


