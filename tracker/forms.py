from typing import Text
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from django.conf import settings
from django.db.models import fields
from django.db.models.fields import files
from django.db.models.fields.related import ForeignKey
from django.db.models.fields.reverse_related import OneToOneRel
from django.forms import ModelForm, widgets
from django.forms.fields import DateField, IntegerField
from django.forms.widgets import *
from .models import *
from django.core.validators import *
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget, PhoneNumberPrefixWidget



class RegisterForm(UserCreationForm):
    last_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'placeholder': 'Last Name..'}))
    first_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'placeholder': 'First Name..'}))
    email = forms.EmailField(max_length=254, help_text='Required. Input a valid email address.',widget=forms.TextInput(attrs={'placeholder': 'Email..'}) )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class PhysicianForm(ModelForm):
    cell_no = PhoneNumberField(
        widget=PhoneNumberInternationalFallbackWidget, required=False
    )
    class Meta:
        model = Physician
        fields = "__all__"

class CreateRecordFormPatient(ModelForm):
    cell_no = PhoneNumberField(
        widget=PhoneNumberInternationalFallbackWidget, required=False,
    )
    cell_no.widget.attrs = {'class': 'form-control', 'placeholder': '+63'}

    mcontact = PhoneNumberField(
        widget=PhoneNumberInternationalFallbackWidget, required=False 
    )
    mcontact.widget.attrs = {'class': 'form-control', 'id': 'mcontact', 'placeholder': '+63'}

    fcontact = PhoneNumberField(
        widget=PhoneNumberInternationalFallbackWidget, required=False 
    )
    fcontact.widget.attrs = {'class': 'form-control', 'id': 'fcontact', 'placeholder': '+63'}

    c1contact = PhoneNumberField(
        widget=PhoneNumberInternationalFallbackWidget, required=False
    )
    c1contact.widget.attrs = {'class': 'form-control', 'id': 'c1contact', 'placeholder': '+63'}

    c2contact = PhoneNumberField(
        widget=PhoneNumberInternationalFallbackWidget, required=False
    )
    c2contact.widget.attrs = {'class': 'form-control', 'id': 'c2contact', 'placeholder': '+63'}

    birthdate = forms.DateField(
        widget=DateInput(
            attrs={'class': 'form-control', 'id': 'dob', 'placeholder': 'mm-dd-yyyy'},
            format='%m-%d-%Y',
        ),
        input_formats=['%m-%d-%Y']
    )
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'middle_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
            'suffix': TextInput(attrs={'class': 'form-control', 'placeholder': 'Suffix'}),
            'nick_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nickname'}),
            'sex': Select(attrs={'class': 'form-control', 'placeholder': 'Sex'}),
            'age': HiddenInput(attrs={'type': 'hidden'}),

            'username': HiddenInput(attrs={'type': 'hidden'}),
            'relationship': TextInput(attrs={'class': 'form-control', 'placeholder': 'Relationship'}),

            'cert_date': HiddenInput(attrs={'type': 'hidden'}),
            
            'attending_doctor': Select(attrs={'class': 'form-control', 'placeholder': 'Attending Doctor'}),
            'landline': TextInput(attrs={'class': 'form-control', 'placeholder': 'Home/Landline'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            
            'house_no': TextInput(attrs={'class': 'form-control', 'placeholder': 'House/Unit no/LtBlk/Street'}),
            'barangay': TextInput(attrs={'class': 'form-control', 'placeholder': 'Barangay'}),
            'city': TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'region': TextInput(attrs={'class': 'form-control', 'placeholder': 'Region'}),
            'zip': TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),

            'mfname': TextInput(attrs={'class': 'form-control', 'id': 'mfname', 'placeholder': 'First Name'}),
            'mlname': TextInput(attrs={'class': 'form-control', 'id': 'mlname', 'placeholder': 'Last Name'}),
            'memail': TextInput(attrs={'class': 'form-control', 'id': 'memail', 'placeholder': 'Email'}),

            'ffname': TextInput(attrs={'class': 'form-control', 'id': 'ffname', 'placeholder': 'First Name'}),
            'flname': TextInput(attrs={'class': 'form-control', 'id': 'flname', 'placeholder': 'Last Name'}),
            'femail': TextInput(attrs={'class': 'form-control', 'id': 'femail', 'placeholder': 'Email'}),

            'c1full_name': TextInput(attrs={'class': 'form-control', 'id': 'c1full_name', 'placeholder': 'Full Name'}),
            'relation1': TextInput(attrs={'class': 'form-control', 'id': 'relation1', 'placeholder': 'Relation'}),
            'c2full_name': TextInput(attrs={'class': 'form-control', 'id': 'c2full_name', 'placeholder': 'Full Name'}),
            'relation2': TextInput(attrs={'class': 'form-control', 'id': 'relation2', 'placeholder': 'Relation'}),   
        }


class AppointmentForm(ModelForm):
    date = forms.DateField(
        widget=DateInput(
            attrs={'class': 'form-control', 'id': 'date', 'placeholder': 'mm-dd-yyyy'},
            format='%m-%d-%Y',
        ),
        input_formats=['%m-%d-%Y']
    )
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'patient': HiddenInput(attrs={'type': 'hidden'}),
            'status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Status'}),
            'time': forms.NumberInput(attrs={'type': 'time', 'class': 'form-control', 'placeholder': 'Time'}),
            'doctor': Select(attrs={'class': 'form-control', 'placeholder': 'Doctor'}),
            'visit': TextInput(attrs={'class': 'form-control', 'placeholder': 'Visit'}),
            'location': TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
        }

class PortalForm(UserCreationForm):
    password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True,}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'required': True,}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': True}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': True,}),
        }

class PatientUserForm(ModelForm):
    class Meta:
        model = PatientUser
        fields = ('relationship',)
        widgets = {
            'relationship': TextInput(attrs={'class': 'form-control', 'placeholder': 'Relationship'}),
        }

class PatientVaccineForm(ModelForm):
    bcg_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    hepb1_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    hepb2_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    dt1_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    ip1_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    hi1_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    pcv1_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    rota1_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    dt2_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    ip2_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    hi2_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    pcv2_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    rota2_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    hepb3_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    dt3_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    ip3_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    hi3_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    pcv3_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    rota3_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    influ1of2_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    measles_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    jap1of2_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    influ2of2_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False) 
    mmr1_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    vari1_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    dtbooster1_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    ipbooster1_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    hibooster1_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    pcvbooster1_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    inacthepa1_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    inacthepa2_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    mening_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    typhoid_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    jap2of2_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    dtbooster2_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    ipbooster2_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    mmr2_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    vari2_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    tdbooster3_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    hpv1of2_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    hpv2of2_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    hpv1of3_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    hpv2of3_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    hpv3of3_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'mm-dd-yyyy'}, format='%m-%d-%Y'), input_formats=['%m-%d-%Y'], required=False)
    
    class Meta:
        model = Patient
        fields = (
            'bcg_brand', 'hepb1_brand', 'hepb2_brand', 'dt1_brand', 'ip1_brand', 'hi1_brand', 'pcv1_brand', 'rota1_brand', 'dt2_brand',
            'ip2_brand', 'hi2_brand', 'pcv2_brand', 'rota2_brand', 'hepb3_brand', 'dt3_brand', 'ip3_brand', 'hi3_brand', 'pcv3_brand',
            'rota3_brand', 'influ1of2_brand', 'measles_brand', 'jap1of2_brand', 'influ2of2_brand', 'mmr1_brand', 'vari1_brand', 'dtbooster1_brand',
            'ipbooster1_brand', 'hibooster1_brand', 'pcvbooster1_brand', 'inacthepa1_brand', 'inacthepa2_brand', 'mening_brand', 'typhoid_brand',
            'jap2of2_brand', 'dtbooster2_brand', 'ipbooster2_brand', 'mmr2_brand', 'vari2_brand', 'tdbooster3_brand', 'hpv1of2_brand', 'hpv2of2_brand',
            'hpv1of3_brand', 'hpv2of3_brand', 'hpv3of3_brand',

            'bcg_date', 'hepb1_date', 'hepb2_date', 'dt1_date', 'ip1_date', 'hi1_date', 'pcv1_date', 'rota1_date', 'dt2_date',
            'ip2_date', 'hi2_date', 'pcv2_date', 'rota2_date', 'hepb3_date', 'dt3_date', 'ip3_date', 'hi3_date', 'pcv3_date',
            'rota3_date', 'influ1of2_date', 'measles_date', 'jap1of2_date', 'influ2of2_date', 'mmr1_date', 'vari1_date', 'dtbooster1_date',
            'ipbooster1_date', 'hibooster1_date', 'pcvbooster1_date', 'inacthepa1_date', 'inacthepa2_date', 'mening_date', 'typhoid_date',
            'jap2of2_date', 'dtbooster2_date', 'ipbooster2_date', 'mmr2_date', 'vari2_date', 'tdbooster3_date', 'hpv1of2_date', 'hpv2of2_date',
            'hpv1of3_date', 'hpv2of3_date', 'hpv3of3_date',

            'bcg_loc', 'hepb1_loc', 'hepb2_loc', 'dt1_loc', 'ip1_loc', 'hi1_loc', 'pcv1_loc', 'rota1_loc', 'dt2_loc',
            'ip2_loc', 'hi2_loc', 'pcv2_loc', 'rota2_loc', 'hepb3_loc', 'dt3_loc', 'ip3_loc', 'hi3_loc', 'pcv3_loc',
            'rota3_loc', 'influ1of2_loc', 'measles_loc', 'jap1of2_loc', 'influ2of2_loc', 'mmr1_loc', 'vari1_loc', 'dtbooster1_loc',
            'ipbooster1_loc', 'hibooster1_loc', 'pcvbooster1_loc', 'inacthepa1_loc', 'inacthepa2_loc', 'mening_loc', 'typhoid_loc',
            'jap2of2_loc', 'dtbooster2_loc', 'ipbooster2_loc', 'mmr2_loc', 'vari2_loc', 'tdbooster3_loc', 'hpv1of2_loc', 'hpv2of2_loc',
            'hpv1of3_loc', 'hpv2of3_loc', 'hpv3of3_loc',

            'bcg_remarks', 'hepb1_remarks', 'hepb2_remarks', 'dt1_remarks', 'ip1_remarks', 'hi1_remarks', 'pcv1_remarks', 'rota1_remarks', 'dt2_remarks',
            'ip2_remarks', 'hi2_remarks', 'pcv2_remarks', 'rota2_remarks', 'hepb3_remarks', 'dt3_remarks', 'ip3_remarks', 'hi3_remarks', 'pcv3_remarks',
            'rota3_remarks', 'influ1of2_remarks', 'measles_remarks', 'jap1of2_remarks', 'influ2of2_remarks', 'mmr1_remarks', 'vari1_remarks', 'dtbooster1_remarks',
            'ipbooster1_remarks', 'hibooster1_remarks', 'pcvbooster1_remarks', 'inacthepa1_remarks', 'inacthepa2_remarks', 'mening_remarks', 'typhoid_remarks',
            'jap2of2_remarks', 'dtbooster2_remarks', 'ipbooster2_remarks', 'mmr2_remarks', 'vari2_remarks', 'tdbooster3_remarks', 'hpv1of2_remarks', 'hpv2of2_remarks',
            'hpv1of3_remarks', 'hpv2of3_remarks', 'hpv3of3_remarks',
        )
        
        
