from django.shortcuts import render, redirect
from .forms import ContactForm
from django.views.generic import TemplateView
from index import forms
from django.core.mail import send_mail

def index(request):
        return render(request, 'index/index.html')

def theteam(request):
        return render(request, 'index/theteam.html')

def services(request):
        return render(request, 'index/services.html')

def quotes(request):
        form = forms.Quote_form()
        form.fields['from_property'].initial = "Property Type"


        if request.method == 'POST':
            form = forms.Quote_form(request.POST)

            if form.is_valid():
                form.save(commit=True)
                return thanks(request)
            else:
                print("Nah")

        return render(request, 'index/quotes.html',  { 'quotes': form })

def insurance(request):
        ins_form = forms.Insurance_form()

        if request.method== "POST":
            ins_form = forms.Insurance_form(request.POST)

            if ins_form.is_valid():
            #    print("VALIDATION SUCCESS")
            #    print("Username: " +form.cleaned_data['username']) #grab cleaned data based on forms instances
            #    print("Password: " +form.cleaned_data['password'])
                ins_form.save(commit=True)
                return thanks(request)
            else:
                print("Nah")

        return render(request,'index/insurance.html',{"insurance_stuff":ins_form })

def contact(request):
        contact_us = forms.Contact_form()

        if request.method== "POST":
            contact_us = forms.Contact_form(request.POST)

            if contact_us.is_valid():
                subject = contact_us.cleaned_data['your_name']
                message = contact_us.cleaned_data['comment']
                sender = contact_us.cleaned_data['your_email']
                #cc_myself = contact_us.cleaned_data['cc_myself']

                recipients = ['nomadservicesny@gmail.com']
                #if cc_myself:

                    #recipients.append(sender)

                    #send_mail(subject, message, sender, recipients)
                    #return HttpResponseRedirect('/thanks/')"""
            #    print("VALIDATION SUCCESS")
            #    print("Username: " +form.cleaned_data['username']) #grab cleaned data based on forms instances
            #    print("Password: " +form.cleaned_data['password'])
                contact_us.save(commit=True)
                return thanks(request)
            else:
                print("Nah")
        return render(request, 'index/contact.html', {"contact_us":contact_us})

def thanks(request):
        return render(request, 'index/thanks.html')

def login(request):
    form = forms.Login_Form()

    if request.method== "POST":
        form = forms.Login_Form(request.POST)

        if form.is_valid():

            print("VALIDATION SUCCESS")
        #    print("Username: " +form.cleaned_data['username']) #grab cleaned data based on forms instances
        #    print("Password: " +form.cleaned_data['password'])
            form.save(commit=True)
            return index(request)
        else:
            print("Nah")

    return render(request,'index/login.html',{"login_stuff":form })


    #class HomeView(TemplateView):
    #  template_name = 'index/templates/index/quotes.html'

 #   def get_name(self, request):
   #     form = NameForm()
   #     if form.is_valid():
    #            return HttpResponseRedirect('/thanks/')

   # return render(request, self.template_name, { 'form': form })

def form(request):
    form = forms.ContactForm()

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)

    return render(request, 'index/form.html',  { 'form': form })

# Create your views here.
