from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from Mobileapp.models import *

class UsersignupForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"Enter Password",
		}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"Enter Confirm Password",
		}))

	class Meta:
		model = User
		fields = ["username","first_name","last_name","email"]
		widgets = {
			"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Your Username",
			"required":True,
			}),
			"first_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter First name",
			"required":True,
			}),
			"last_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Last name",
			"required":True,
			}),
			"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Enter EmailId",
			"required":True,
			}),
		}

class updateform(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name','email']
		widgets={
		"username":forms.TextInput(attrs={'class':'form-control','placeholder':'enter username','required':True}),
		"first_name":forms.TextInput(attrs={'class':'form-control','placeholder':'enter first_name','required':True}),
		"last_name":forms.TextInput(attrs={'class':'form-control','placeholder':'enter last_name','required':True}),
		"email":forms.TextInput(attrs={'class':'form-control','placeholder':'enter email','required':True}),
		}

class imageprofile(forms.ModelForm):
	class Meta:
		model = update
		fields = ["age","gender","image"]
		widgets ={
		"age":forms.NumberInput(attrs={
			"class":"form-control",
			}),
		"gender":forms.Select(attrs={
			"class":"form-control",
			}),
		}

# class ProductForm(forms.ModelForm):
# 	class Meta:
# 		model = product
# 		fields = '__all__'

# 		widgets={
# 		"name":forms.TextInput(attrs={'placeholder':"Enter name",'class':"form-control"}),
# 		"age":forms.NumberInput(attrs={'placeholder':"Enter price",'class':"form-control"}),
# 		"category":forms.ModelChoiceField(attrs={'class':"form-control"}),
# 		"description":forms.RadioSelect(attrs={'class':"radio-inline"}),
# 		"image":forms.Select(attrs={'class':"form-control"}),
# 		}
