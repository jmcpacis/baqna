from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, DateField, TimeField
from django.forms import widgets
from django.forms.fields import ChoiceField
from django.urls import reverse
from django.core.validators import *
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Physician(models.Model):
    # user = models.OneToOneField(User, limit_choices_to={'groups__name':u'Physician'}, null=True, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    cell_no = PhoneNumberField(null=True, blank=True)
    specialization = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return self.last_name + ", " + self.first_name + ' - ' + self.specialization
    
    def get_absolute_url(self):
        return reverse('updatePhysician', args=[str(self.pk)])


class Patient(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    last_name = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    suffix = models.CharField(max_length=2, null=True, blank=True)
    nick_name = models.CharField(max_length=100, null=True, blank=True)
    sex = models.CharField(max_length=1, null=True, choices=SEX)
    birthdate = models.DateField(null=True)
    age = models.CharField(max_length=100, null=True, blank=True)
    attending_doctor = models.ForeignKey(Physician, related_name="docpatient", on_delete=models.CASCADE, null=True)

    #Vaccine Certificate Date
    cert_date = models.DateField(null=True, blank=True)

    # Contact Deets
    cell_no = PhoneNumberField(null=True, blank=True, validators=[MaxLengthValidator(13)])
    landline = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    
    # Address
    house_no = models.CharField(max_length=100, null=True, blank=True)
    barangay = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    
    # Mother
    mfname = models.CharField(max_length=100, null=True, blank=True)
    mlname = models.CharField(max_length=100, null=True, blank=True)
    mcontact = PhoneNumberField(null=True, blank=True)
    memail = models.EmailField(max_length=254, null=True, blank=True)
    # Father
    ffname = models.CharField(max_length=100, null=True, blank=True)
    flname = models.CharField(max_length=100, null=True, blank=True)
    fcontact = PhoneNumberField(null=True, blank=True)
    femail = models.EmailField(max_length=254, null=True, blank=True)

    c1full_name = models.CharField(max_length=100, null=True, blank=True)
    relation1 = models.CharField(max_length=100, null=True, blank=True)
    c1contact = PhoneNumberField(null=True, blank=True)

    c2full_name = models.CharField(max_length=100, null=True, blank=True)
    relation2 = models.CharField(max_length=100, null=True, blank=True)
    c2contact = PhoneNumberField(null=True, blank=True)

    # Vaccine Brands
    bcg_brand = models.CharField(max_length=100, null=True, blank=True)
    hepb1_brand = models.CharField(max_length=100, null=True, blank=True)
    hepb2_brand = models.CharField(max_length=100, null=True, blank=True)
    dt1_brand = models.CharField(max_length=100, null=True, blank=True)
    ip1_brand = models.CharField(max_length=100, null=True, blank=True)
    hi1_brand = models.CharField(max_length=100, null=True, blank=True)
    pcv1_brand = models.CharField(max_length=100, null=True, blank=True)
    rota1_brand = models.CharField(max_length=100, null=True, blank=True)
    dt2_brand = models.CharField(max_length=100, null=True, blank=True)
    ip2_brand = models.CharField(max_length=100, null=True, blank=True)
    hi2_brand = models.CharField(max_length=100, null=True, blank=True)
    pcv2_brand = models.CharField(max_length=100, null=True, blank=True)
    rota2_brand = models.CharField(max_length=100, null=True, blank=True)
    hepb3_brand = models.CharField(max_length=100, null=True, blank=True)
    dt3_brand = models.CharField(max_length=100, null=True, blank=True)
    ip3_brand = models.CharField(max_length=100, null=True, blank=True)
    hi3_brand = models.CharField(max_length=100, null=True, blank=True)
    pcv3_brand = models.CharField(max_length=100, null=True, blank=True)
    rota3_brand = models.CharField(max_length=100, null=True, blank=True)
    influ1of2_brand = models.CharField(max_length=100, null=True, blank=True)
    measles_brand = models.CharField(max_length=100, null=True, blank=True)
    jap1of2_brand = models.CharField(max_length=100, null=True, blank=True)
    influ2of2_brand = models.CharField(max_length=100, null=True, blank=True) 
    mmr1_brand = models.CharField(max_length=100, null=True, blank=True)
    vari1_brand = models.CharField(max_length=100, null=True, blank=True)
    dtbooster1_brand = models.CharField(max_length=100, null=True, blank=True)
    ipbooster1_brand = models.CharField(max_length=100, null=True, blank=True)
    hibooster1_brand = models.CharField(max_length=100, null=True, blank=True)
    pcvbooster1_brand = models.CharField(max_length=100, null=True, blank=True)
    inacthepa1_brand = models.CharField(max_length=100, null=True, blank=True)
    inacthepa2_brand = models.CharField(max_length=100, null=True, blank=True)
    mening_brand = models.CharField(max_length=100, null=True, blank=True)
    typhoid_brand = models.CharField(max_length=100, null=True, blank=True)
    jap2of2_brand = models.CharField(max_length=100, null=True, blank=True)
    dtbooster2_brand = models.CharField(max_length=100, null=True, blank=True)
    ipbooster2_brand = models.CharField(max_length=100, null=True, blank=True)
    mmr2_brand = models.CharField(max_length=100, null=True, blank=True)
    vari2_brand = models.CharField(max_length=100, null=True, blank=True)
    tdbooster3_brand = models.CharField(max_length=100, null=True, blank=True)
    hpv1of2_brand = models.CharField(max_length=100, null=True, blank=True)
    hpv2of2_brand = models.CharField(max_length=100, null=True, blank=True)
    hpv1of3_brand = models.CharField(max_length=100, null=True, blank=True)
    hpv2of3_brand = models.CharField(max_length=100, null=True, blank=True)
    hpv3of3_brand = models.CharField(max_length=100, null=True, blank=True)

    # Vaccine Date
    bcg_date = models.DateField(null=True, blank=True)
    hepb1_date = models.DateField(null=True, blank=True)
    hepb2_date = models.DateField(null=True, blank=True)
    dt1_date = models.DateField(null=True, blank=True)
    ip1_date = models.DateField(null=True, blank=True)
    hi1_date = models.DateField(null=True, blank=True)
    pcv1_date = models.DateField(null=True, blank=True)
    rota1_date = models.DateField(null=True, blank=True)
    dt2_date = models.DateField(null=True, blank=True)
    ip2_date = models.DateField(null=True, blank=True)
    hi2_date = models.DateField(null=True, blank=True)
    pcv2_date = models.DateField(null=True, blank=True)
    rota2_date = models.DateField(null=True, blank=True)
    hepb3_date = models.DateField(null=True, blank=True)
    dt3_date = models.DateField(null=True, blank=True)
    ip3_date = models.DateField(null=True, blank=True)
    hi3_date = models.DateField(null=True, blank=True)
    pcv3_date = models.DateField(null=True, blank=True)
    rota3_date = models.DateField(null=True, blank=True)
    influ1of2_date = models.DateField(null=True, blank=True)
    measles_date = models.DateField(null=True, blank=True)
    jap1of2_date = models.DateField(null=True, blank=True)
    influ2of2_date = models.DateField(null=True, blank=True) 
    mmr1_date = models.DateField(null=True, blank=True)
    vari1_date = models.DateField(null=True, blank=True)
    dtbooster1_date = models.DateField(null=True, blank=True)
    ipbooster1_date = models.DateField(null=True, blank=True)
    hibooster1_date = models.DateField(null=True, blank=True)
    pcvbooster1_date = models.DateField(null=True, blank=True)
    inacthepa1_date = models.DateField(null=True, blank=True)
    inacthepa2_date = models.DateField(null=True, blank=True)
    mening_date = models.DateField(null=True, blank=True)
    typhoid_date = models.DateField(null=True, blank=True)
    jap2of2_date = models.DateField(null=True, blank=True)
    dtbooster2_date = models.DateField(null=True, blank=True)
    ipbooster2_date = models.DateField(null=True, blank=True)
    mmr2_date = models.DateField(null=True, blank=True)
    vari2_date = models.DateField(null=True, blank=True)
    tdbooster3_date = models.DateField(null=True, blank=True)
    hpv1of2_date = models.DateField(null=True, blank=True)
    hpv2of2_date = models.DateField(null=True, blank=True)
    hpv1of3_date = models.DateField(null=True, blank=True)
    hpv2of3_date = models.DateField(null=True, blank=True)
    hpv3of3_date = models.DateField(null=True, blank=True)

    # Vaccine Location
    bcg_loc = models.CharField(max_length=100, null=True, blank=True)
    hepb1_loc = models.CharField(max_length=100, null=True, blank=True)
    hepb2_loc = models.CharField(max_length=100, null=True, blank=True)
    dt1_loc = models.CharField(max_length=100, null=True, blank=True)
    ip1_loc = models.CharField(max_length=100, null=True, blank=True)
    hi1_loc = models.CharField(max_length=100, null=True, blank=True)
    pcv1_loc = models.CharField(max_length=100, null=True, blank=True)
    rota1_loc = models.CharField(max_length=100, null=True, blank=True)
    dt2_loc = models.CharField(max_length=100, null=True, blank=True)
    ip2_loc = models.CharField(max_length=100, null=True, blank=True)
    hi2_loc = models.CharField(max_length=100, null=True, blank=True)
    pcv2_loc = models.CharField(max_length=100, null=True, blank=True)
    rota2_loc = models.CharField(max_length=100, null=True, blank=True)
    hepb3_loc = models.CharField(max_length=100, null=True, blank=True)
    dt3_loc = models.CharField(max_length=100, null=True, blank=True)
    ip3_loc = models.CharField(max_length=100, null=True, blank=True)
    hi3_loc = models.CharField(max_length=100, null=True, blank=True)
    pcv3_loc = models.CharField(max_length=100, null=True, blank=True)
    rota3_loc = models.CharField(max_length=100, null=True, blank=True)
    influ1of2_loc = models.CharField(max_length=100, null=True, blank=True)
    measles_loc = models.CharField(max_length=100, null=True, blank=True)
    jap1of2_loc = models.CharField(max_length=100, null=True, blank=True)
    influ2of2_loc = models.CharField(max_length=100, null=True, blank=True) 
    mmr1_loc = models.CharField(max_length=100, null=True, blank=True)
    vari1_loc = models.CharField(max_length=100, null=True, blank=True)
    dtbooster1_loc = models.CharField(max_length=100, null=True, blank=True)
    ipbooster1_loc = models.CharField(max_length=100, null=True, blank=True)
    hibooster1_loc = models.CharField(max_length=100, null=True, blank=True)
    pcvbooster1_loc = models.CharField(max_length=100, null=True, blank=True)
    inacthepa1_loc = models.CharField(max_length=100, null=True, blank=True)
    inacthepa2_loc = models.CharField(max_length=100, null=True, blank=True)
    mening_loc = models.CharField(max_length=100, null=True, blank=True)
    typhoid_loc = models.CharField(max_length=100, null=True, blank=True)
    jap2of2_loc = models.CharField(max_length=100, null=True, blank=True)
    dtbooster2_loc = models.CharField(max_length=100, null=True, blank=True)
    ipbooster2_loc = models.CharField(max_length=100, null=True, blank=True)
    mmr2_loc = models.CharField(max_length=100, null=True, blank=True)
    vari2_loc = models.CharField(max_length=100, null=True, blank=True)
    tdbooster3_loc = models.CharField(max_length=100, null=True, blank=True)
    hpv1of2_loc = models.CharField(max_length=100, null=True, blank=True)
    hpv2of2_loc = models.CharField(max_length=100, null=True, blank=True)
    hpv1of3_loc = models.CharField(max_length=100, null=True, blank=True)
    hpv2of3_loc = models.CharField(max_length=100, null=True, blank=True)
    hpv3of3_loc = models.CharField(max_length=100, null=True, blank=True)

    # Vaccine Remarks
    bcg_remarks = models.CharField(max_length=100, null=True, blank=True)
    hepb1_remarks = models.CharField(max_length=100, null=True, blank=True)
    hepb2_remarks = models.CharField(max_length=100, null=True, blank=True)
    dt1_remarks = models.CharField(max_length=100, null=True, blank=True)
    ip1_remarks = models.CharField(max_length=100, null=True, blank=True)
    hi1_remarks = models.CharField(max_length=100, null=True, blank=True)
    pcv1_remarks = models.CharField(max_length=100, null=True, blank=True)
    rota1_remarks = models.CharField(max_length=100, null=True, blank=True)
    dt2_remarks = models.CharField(max_length=100, null=True, blank=True)
    ip2_remarks = models.CharField(max_length=100, null=True, blank=True)
    hi2_remarks = models.CharField(max_length=100, null=True, blank=True)
    pcv2_remarks = models.CharField(max_length=100, null=True, blank=True)
    rota2_remarks = models.CharField(max_length=100, null=True, blank=True)
    hepb3_remarks = models.CharField(max_length=100, null=True, blank=True)
    dt3_remarks = models.CharField(max_length=100, null=True, blank=True)
    ip3_remarks = models.CharField(max_length=100, null=True, blank=True)
    hi3_remarks = models.CharField(max_length=100, null=True, blank=True)
    pcv3_remarks = models.CharField(max_length=100, null=True, blank=True)
    rota3_remarks = models.CharField(max_length=100, null=True, blank=True)
    influ1of2_remarks = models.CharField(max_length=100, null=True, blank=True)
    measles_remarks = models.CharField(max_length=100, null=True, blank=True)
    jap1of2_remarks = models.CharField(max_length=100, null=True, blank=True)
    influ2of2_remarks = models.CharField(max_length=100, null=True, blank=True) 
    mmr1_remarks = models.CharField(max_length=100, null=True, blank=True)
    vari1_remarks = models.CharField(max_length=100, null=True, blank=True)
    dtbooster1_remarks = models.CharField(max_length=100, null=True, blank=True)
    ipbooster1_remarks = models.CharField(max_length=100, null=True, blank=True)
    hibooster1_remarks = models.CharField(max_length=100, null=True, blank=True)
    pcvbooster1_remarks = models.CharField(max_length=100, null=True, blank=True)
    inacthepa1_remarks = models.CharField(max_length=100, null=True, blank=True)
    inacthepa2_remarks = models.CharField(max_length=100, null=True, blank=True)
    mening_remarks = models.CharField(max_length=100, null=True, blank=True)
    typhoid_remarks = models.CharField(max_length=100, null=True, blank=True)
    jap2of2_remarks = models.CharField(max_length=100, null=True, blank=True)
    dtbooster2_remarks = models.CharField(max_length=100, null=True, blank=True)
    ipbooster2_remarks = models.CharField(max_length=100, null=True, blank=True)
    mmr2_remarks = models.CharField(max_length=100, null=True, blank=True)
    vari2_remarks = models.CharField(max_length=100, null=True, blank=True)
    tdbooster3_remarks = models.CharField(max_length=100, null=True, blank=True)
    hpv1of2_remarks = models.CharField(max_length=100, null=True, blank=True)
    hpv2of2_remarks = models.CharField(max_length=100, null=True, blank=True)
    hpv1of3_remarks = models.CharField(max_length=100, null=True, blank=True)
    hpv2of3_remarks = models.CharField(max_length=100, null=True, blank=True)
    hpv3of3_remarks = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)

class PatientUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    relationship = models.CharField(max_length=50, null=True)

    def __str__(self):
        return '{} of {}'.format(self.relationship, self.patient)


class Appointment(models.Model):
    STATUS = (
        ('Blank','Blank'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Rescheduled', 'Rescheduled'),
        ('Requested', 'Requested'),
    )
    patient = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS, null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    doctor = models.ForeignKey(Physician, on_delete=models.CASCADE)
    visit = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.patient)