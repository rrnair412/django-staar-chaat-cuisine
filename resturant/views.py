from django.shortcuts import render, redirect
from django.core.mail import send_mail


def home(request):
    return render(request, 'resturant/home.html', {'body_class': 'homepage'})

def about(request):
    return render(request, 'resturant/about.html')

def contact(request):
  if request.method == 'GET':
    return render(request, 'resturant/contact.html')
  else:
  	print('i am post')
  	fname = request.POST['full_name']
  	email = request.POST['email']
  	phone = request.POST['phone']
  	message = request.POST['message']
  	send_mail(
      'Cusotmer Inquiry From Website',
      'Message: ' + message + '. First Name: ' + fname + '. Customer Phone Number: ' + phone + '. Customer Email Address: ' + email +'. Please check and respond Accordingly',
      email,
      ['customerservice.starchaat@gmail.com'],
      fail_silently=False
    )
  	return redirect('/about/')
     

def menu(request):
    return render(request, 'resturant/menu.html')

def gallery(request):
    return render(request, 'resturant/gallery.html')

def catering(request):
    return render(request, 'resturant/catering.html')