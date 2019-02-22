from django.shortcuts import render
from admin_app.forms import UserForm, UserProfileForm

def index(request):
    return render(request,'admin_app/index.html')

def register(request):

    registered = False  #check if registered and set equal to false - assume not registered

    if request.method == "POST":
        user_form = UserForm(data=request.POST)                     #*********
        profile_form = UserProfileForm(data=request.POST)           #grabs information from both forms

        if user_form.is_valid() and profile_form.is_valid():        #check if both forms are valid

            user = user_form.save()     #grab everything from base user form
            user.set_password(user.password)        #Hashes password
            user.save()     #save

            profile = profile_form.save()
            profile.user = user     #the user form goes into the user's profile

            if 'profile_pic' in request.FILES:      #other types of files too resume, pdf, csv
                profile.profile_pic = request.FILES['profile_pic']  #this key is what you defined in the models

            profile.save()      #save profile if there was a pic

            registered = True

        else:    #if both forms are vaild (set up profile and pic )
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'admin_app/registration.html',
                            {'user_form': user_form,
                            'profile_form':profile_form,
                            'registered':registered})
# Create your views here.

def farmer(request):
    return render(request,'admin_app/farmer.html')
