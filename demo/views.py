from django.shortcuts import render,redirect
from django.http import HttpResponse

from . import models

# Create your views here.

def demo(request):
    # return HttpResponse('Hello, World!')
    person = {
        'name': 'john doe',
        'age': 30,
        'hobbies': ['Cinema', 'Sports', 'Music', 'Programming'],
        'gender': 'M'
    }
    location = "Dhaka"
    return render(request, 'index.html', {'location':location, 'person':person})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        #return HttpResponse(f'name = {name} email = {email} subject = {subject} message = {message}') comes in url 
        #save in database 
        #creating query object 
        Query = models.Query(name = name,email=email,subject=subject,message=message)

        Query.save()

        return redirect('contact')

    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def greet(request, mynum,p,person):

    print(mynum,p,person)

    #this are for query parameter ?p=100&&xyz=check&&display=hi&&xyz=/user
    
    display = request.GET.get('display','Default Value') #if i don't give default then will come none 
    page_number = request.GET.get('p',1)

    xyz = request.GET.get('xyz','default')

    get_value = request.GET.get('person') #we don't have any key as person inside request.GET dictionary 
    #so if we print get_value output will be none , if the does not exist then will be assign none. 

    print(xyz)

    

    print(get_value)

    print(request.GET)

    print(request.GET.get('xyz')) #will give the last value of corrosponding key 

    print(request.GET.getlist('xyz')[0]) #for getting all the values use getlist('key') will return a list , can 
    #be accessable with subscript 

    return render(request, 'person.html', {'person':person,'display':display, 'page_number':page_number})

def favnum(request, n):
    return HttpResponse('Your favorite number is: ' + str(n))


def notice(request):
    #getting notice from the database 
    notices = models.Notice.objects.all()
    print(notices)
    return render(request,'notice.html',{'notices' : notices}) #passing notices as context 
    