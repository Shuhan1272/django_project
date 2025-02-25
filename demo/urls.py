from django.urls import path
from . import views

urlpatterns = [

    # Note : without giving forward slash at the end of each url sepration link will not work 

    path('demo/', views.demo, name='demo'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),

    #dynamic urls : check dynamic_url_work.py for more clearification 

    path('user/<person>/<p>/<int:mynum>/', views.greet, name='greet'), 
    
    #inside the greet function person=from_url,p=from_url,and mynum=form_url [must be number] will pass as keyword arguments
    #so greet function must these arguments with exact name of parameter 

    path('favorite/<int:n>/',views.favnum, name='favnum')
]