from django import forms
from index.models import Login_Model, Quote,PROP_CHOICES,FLIGHT_CHOICES,YON, Insurance, Comment, REF_LIST
from django.core import validators
from django.forms import Textarea, TextInput

class ContactForm(forms.Form):
    your_name = forms.CharField(max_length=100)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'fieldWrapper','placeholder':'Enter your email'}))
    num = forms.CharField(widget=forms.NumberInput(attrs={'class':'fieldWrapper','placeholder':'Enter your number'}))


class Login_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'required': True,'class':'inputs'}),label='')

    class Meta:
        model = Login_Model
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username','class':'inputs'}),
        }
        labels = {'username': ''}

class Quote_form(forms.ModelForm):

    widgets = {
        'flights_from': forms.Select(choices=FLIGHT_CHOICES,attrs={'class': 'form_inputs'}),
        'flights_to': forms.Select(choices=FLIGHT_CHOICES,attrs={'class': 'form_inputs'}),
        'from_property': forms.Select(choices=PROP_CHOICES,attrs={'class': 'form_inputs'}),
        'insurance':forms.RadioSelect(choices=YON,attrs={'class': 'form_inputs'}),
        'referral': forms.Select(choices=REF_LIST,attrs={'class': 'form_inputs'})

    }

    class Meta:
    #    CHOICES = (('1', 'First',), ('2', 'Second',))
    #   choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        model = Quote
        fields = '__all__'
        widgets = {

            'name' : forms.TextInput(attrs={'class': 'form_inputs','placeholder':'Enter Your Name'},),
            'email' : forms.TextInput(attrs={'class': 'form_inputs','placeholder':'Enter Your Email'}),
            'from_zip' : forms.TextInput(attrs={'class': 'form_inputs','placeholder':'From Zip Code'}),
            'to_zip' : forms.TextInput(attrs={'class': 'form_inputs','placeholder':'To Zip Code'}),
            'date' : forms.SelectDateWidget(attrs={'class': 'form_inputs','placeholder':'Moving Date'}),
            'truck_size' : forms.NumberInput(attrs={'class': 'form_inputs','placeholder':'Truck Size (in ft)'}),
            'other' : forms.TextInput(attrs={'class': 'form_inputs','placeholder':'Other'}),
            'reff_code' : forms.TextInput(attrs={'class': 'form_inputs','placeholder':'Refferal Code'}),
        }


class Insurance_form(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = '__all__'
        widgets = {

            'name' : forms.TextInput(attrs={'class': 'form_inputs','placeholder':'Enter Your Name'},),
            'email' : forms.TextInput(attrs={'class': 'form_inputs','placeholder':'Enter Your Email'}),
            'from_zip' : forms.TextInput(attrs={'class': 'form_inputs','placeholder':'From Zip Code'}),
            'to_zip' : forms.TextInput(attrs={'class': 'form_inputs','placeholder':'To Zip Code'}),
            'date' : forms.SelectDateWidget(attrs={'class': 'form_inputs','placeholder':'Moving Date'}),
        }
class Contact_form(forms.ModelForm):
    #cc_myself = forms.BooleanField(required=False)

    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name'}),
            'comment': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        labels = {
        'name':'',
        'comment':"Tell us something good!",
        'heard':'How did you hear about us?'
        }
