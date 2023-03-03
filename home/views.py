from multiprocessing import context
from django.http import HttpResponse   # if this line not working use just httpresponse in the down
from django.shortcuts import render
from home.models import Contact, About

# Create your views here.
def home(request):
    # return HttpResponse ("this is a home page result")

    return render(request, 'index.html')



def contact(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']




        print("name, email, message")

        ins = Contact(name=name, email=email, message=message)
        ins.save()

        print("tq for contacting us")





    # return HttpResponse ("this is a contact page result")
    return render(request, 'contact.html')

def about(request):
    about = About.objects.all()
    context = { 'about' : about}

    if request.method == "POST":
        name = request.POST['name']
        number = request.POST['number']
        address = request.POST['address']
        role = request.POST['role']
        emid = request.POST['emid']



        print("name, email, message")

        ins = About(name=name, number=number, address=address , role = role , emid = emid )
        ins.save()

        print("tq for contacting us")





    # return HttpResponse ("this is a contact page result")
    return render(request, 'about.html', context )



