

#Note : urls are passing as keyword arguments as view function 

#it's mean I have to receive all the parameter with exact same name in view function 

#Note : order does not matter for keyword argument recieve but exact name matter 




# def view_fun(**kwargs): one way to recive keywords argument , will recive as dictionary object 
#     print(kwargs) 

# def view_fun(**kwargs): #indivisual recive keyword argument
#     #print(p,person,mynum)
#     print(type(kwargs))
#     print(kwargs['person'])
#     #print(kwargs.person) Note : this will not work , in python dictionary values should access ['key'] can arise error 
#     # to avoid error should use .get('key') will return None if the key doesn't exist. 
#     # for more information check this https://chatgpt.com/c/67bd01a3-7cd4-8002-8394-eb9d1292fe84

# *** Note : As we are working with the keyword argument then arguments name must be same 

def view_fun(person,p,mynum): #this is how dynamic urls work 
    print(p,person,mynum)

view_fun(p=10,person='shuhan',mynum=17) #these keywords arguments will pass from the urls 