from django.forms import ModelForm
from .models import Registration,booking,hotel,room,package
from django import forms

class RegistrationForm(ModelForm):
    class Meta:
        model=Registration
        fields =('username', 'email','phone','password','confirmpassword')

        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),
            'confirmpassword':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Phone Number'}),
        }
CHOICES=[('Yes','Yes'),('No','No')]

class bookingform(ModelForm):
    vechile = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)

    class Meta:
        model=booking
        fields=('username', 'email','phone','check_in','check_out','members','total_rooms','vechile')     
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'Enter Your Name'}),
            'email':forms.TextInput(attrs={'placeholder':'Enter Your Email'}),
            'phone':forms.TextInput(attrs={'placeholder':'+92'}),
            'check_in':forms.DateInput(attrs={'placeholder':'YYYY-MM-DD'}),
            'check_out':forms.DateInput(attrs={'placeholder':'YYYY-MM-DD'}),
            'members':forms.NumberInput(attrs={'placeholder':"2" ,'min':"1"}),
            'total_rooms':forms.NumberInput(attrs={'placeholder':"1" ,'min':"1"}),
            
        }
                

class RegisterHotel(forms.ModelForm):
    class Meta:
        model=hotel
        fields =('name', 'hotel_description','password','hotel_image','city_name')

        widgets ={
            'name':forms.TextInput(attrs={'placeholder':'Enter Your Name'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Enter Password'}),
            'hotel_description':forms.TextInput(attrs={'placeholder':'Enter Description'}),  
            'hotel_image':forms.FileInput(),       
        }

class Room(forms.ModelForm):
    class Meta:
        model=room 
        fields =('room_name', 'room_description','price','room_image')

        widgets ={
            'room_name':forms.TextInput(attrs={'placeholder':'Enter Your Name'}),
            'room_description':forms.TextInput(attrs={'placeholder':'Enter Description'}),
            'price':forms.NumberInput(attrs={'placeholder':'Enter Price','min':"1"}),  
            'room_image':forms.FileInput(),       
        }    

class Package(forms.ModelForm):
    class Meta:
        model=package
        fields =('package_name', 'package_description','price','image')

        widgets ={
            'package_name':forms.TextInput(attrs={'placeholder':'Enter Your Name'}),
            'package_description':forms.TextInput(attrs={'placeholder':'Enter Description'}),
            'price':forms.NumberInput(attrs={'placeholder':'Enter Price','min':"1"}),  
            'image':forms.FileInput(),       
        }                 
        

