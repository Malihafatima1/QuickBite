from django.shortcuts import render
from django.http import HttpResponse
from Base_App1.models import BookTable, AboutUs, Feedback, ItemList, Items


# Create your views here.

def HomeView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    review=Feedback.objects.all()
    return render(request,'home.html',{'items':items, 'list':list,'review':review})


def AboutView(request):
    data=AboutUs.objects.all()
    return render(request, 'about.html',{'data':data})


def MenuView(request):
    items=Items.objects.all()
    list=ItemList.objects.all()
    return render(request, 'menu.html', {'items':items, 'list':list})


def BookTableView(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        total_person = request.POST.get('total_person')
        booking_data = request.POST.get('booking_data')

        if name and phone_number and email and total_person and booking_data:
            data = BookTable(
                Name=name,
                Phone_number=phone_number,
                Email=email,
                Total_person=total_person,
                Booking_data=booking_data
            )
            data.save()
            return render(request, 'book_table.html', {'message': 'Booking successful!'})
        else:
            return render(request, 'book_table.html', {'message': 'Please fill in all fields correctly.'})


    return render(request, 'book_table.html')



from django.shortcuts import render, redirect
from .models import Feedback
from django.core.files.storage import FileSystemStorage

def FeedbackView(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        description = request.POST.get('Description')
        rating = request.POST.get('total_person')  # it's a string, convert to int
        image = request.FILES.get('Image')  # get image from form input

        feedback = Feedback(
            User_name=user_name,
            Description=description,
            Rating=int(rating),
            Image=image
        )
        feedback.save()
        return redirect('Home')  # Redirect to home page after submission

    return render(request, 'feedback.html')
