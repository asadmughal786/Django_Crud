from django.contrib import messages
from django.shortcuts import render , HttpResponseRedirect
from .forms import User_registeration
from .models import App_Users

# Create your views here.

#----------------------------------------------------- This function will add and show all items 
def add_user(request):
    if request.method == "POST":
        
        form = User_registeration(request.POST)
        user_data = {}
        if form.is_valid():
            fname = form.cleaned_data['First_Name']
            lname = form.cleaned_data['Last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            conf_password = form.cleaned_data['confirm_Password']
            # -------------------------- Server Side Validation (Whole Form Validation)---------------------------------------------------------------------
            if password == conf_password:
                user = App_Users(First_Name = fname, Last_name = lname, email=email,password = password, confirm_Password = conf_password)
                user.save()
                messages.success(request,"User Saved Successfully!")
                form = User_registeration()
                user_data = App_Users.objects.all()
                return render(request,'registeration.html',{'form':form,'user_data':user_data})
            else:
                messages.error(request,"Password Does not Mached")
                form = User_registeration()
                user_data = App_Users.objects.all()
        return render(request,'registeration.html', {'form': form,'user_data': user_data})
    else:
        form = User_registeration()
        user_data = App_Users.objects.all()
    return render(request,'registeration.html', {'form': form,'user_data': user_data})

#--------------------------------------------------------This is delete function

def delete_data(request, id):
    if request.method == 'POST':
        data = App_Users.objects.get(pk=id)
        data.delete()
        messages.info(request,"Record has been Deleted!")
        return HttpResponseRedirect('/')

#-------------------------------------------------------Update Form data--------------

def update_form(request,id):
    if request.method == 'POST':
        data = App_Users.objects.get(pk=id)
        form = User_registeration(request.POST, instance=data)

        if form.is_valid():
            
            #user = App_Users(First_Name = fname, Last_name = lname, email=email,password = password, confirm_Password = conf_password)
            form.save()
            messages.success(request,"User updated Successfully!")
    else:
        data =  App_Users.objects.get(pk=id)
        form = User_registeration(instance=data)
        
    return render(request, 'update.html',{'form':form})