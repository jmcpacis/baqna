from django.db.models.query_utils import PathInfo
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from vaccine_tracker.settings import EMAIL_HOST_USER
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .filters import *
import datetime
from xhtml2pdf import pisa
from easy_pdf.views import PDFTemplateResponseMixin, PDFTemplateView
from django.views.generic.detail import DetailView


# Create your views here.
# @login_required(login_url='login')
# @user_passes_test(lambda u: u.is_superuser)
def registerPage(request):
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                last_name = form.cleaned_data.get('last_name')
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                subject = 'Account Registration'
                message = 'Hi Mr./Ms.' + last_name + '! Here are your account credentials for our application.' + ' Username: ' + username + ' Password: ' + raw_password
                recepient = str(form.cleaned_data.get('email'))
            
                send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)

                messages.success(request, 'Account was created for ' + username)
                return redirect('home')
            else:
                messages.error(request, "Unsuccessful registration. Invalid information.")
                
        context = {'form':form}
        return render(request, 'patientmonitoring/register.html', context)

@login_required(login_url='login')
def notifsPage(request):
    return render(request,'patientmonitoring/notifs.html')

def logoutUser(request):
	logout(request)
	return redirect('login')

@unauthenticated_user
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                
                user = authenticate(request, username=username, password=password)
                
                if user is not None:
                    login(request, user)
                    return redirect('home')
                elif username == '' or password == '':
                    messages.info(request, 'Username or password is blank. Please try again.')
                elif username is not None and password == '':
                    messages.info(request, 'Password is blank. Please try again.')
                    context = {username}
                else:
                    messages.info(request, 'Username or password is incorrect. Please try again.')
        context = {}
        return render(request, 'patientmonitoring/login.html', context)



@login_required(login_url='login')
def homePage(request):
    patients = Patient.objects.all()
    patientFilter = PatientFilter(request.GET, queryset=patients)
    patients = patientFilter.qs

    physicians = Physician.objects.all()
    data = {
        'patients': patients, 'physicians': physicians , 'patientFilter': patientFilter,
    }

    return render(request, "patientmonitoring/home.html", data)

#--CREATE RECORD VIEW--
@login_required(login_url='login')
def createRecord(request):
    patient_form = CreateRecordFormPatient()
    latest = Patient.objects.latest('id')
    latest_id = getattr(latest, 'id')

    if(request.method == "POST"):
        patient_form = CreateRecordFormPatient(request.POST)
        if patient_form.is_valid():
            pfname = patient_form.cleaned_data.get('first_name')
            plname = patient_form.cleaned_data.get('last_name')

            patient_form.save()

            messages.success(request, 'Account was created for {} {}.'.format(pfname, plname))
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
        return redirect('/home')

    context = {'patient_form':patient_form,
                'latest_id': latest_id,
    }
    return render(request, "patientmonitoring/createRecord.html", context)
    
@login_required(login_url='login')
def patient(request, pk):
    patient = Patient.objects.get(id=pk)

    # -- Age (X Years Y Months) --
    curr_date = datetime.date.today()
    months = curr_date.month - patient.birthdate.month
    years = curr_date.year - patient.birthdate.year
    age = "{} year {} month".format(years, months)
    
    data = {
        'patient': patient, 'age': age,
    }
    return render(request, 'patientmonitoring/patient.html', data)

@login_required(login_url='login')
def editPatient(request, pk):
    patient = Patient.objects.get(id=pk)
    patient_form = CreateRecordFormPatient(instance=patient)

    # -- Age (X Years Y Months) --
    curr_date = datetime.date.today()
    months = curr_date.month - patient.birthdate.month
    years = curr_date.year - patient.birthdate.year
    age = "{} year {} month".format(years, months)

    if(request.method == "POST"):
        patient_form = CreateRecordFormPatient(request.POST, instance=patient)
        if patient_form.is_valid():
            pfname = patient_form.cleaned_data.get('first_name')
            plname = patient_form.cleaned_data.get('last_name')

            patient_form.save()

            # messages.success(request, 'Account was created for ' + pfname + plname)
            return redirect('/patient/' + pk)

    data = {
        'patient': patient, 
        'patient_form': patient_form,
        'age': age,
    }

    return render(request, 'patientmonitoring/editPatient.html', data)

@login_required(login_url='login')
def appointment(request, pk):
    patient = Patient.objects.get(id=pk)
    appointment_form = AppointmentForm(initial={'patient': patient})

    appointments = Appointment.objects.all()

    # -- Age (X Years Y Months) --
    curr_date = datetime.date.today()
    months = curr_date.month - patient.birthdate.month
    years = curr_date.year - patient.birthdate.year
    age = "{} year {} month".format(years, months)

    if(request.method == "POST"):
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment_form.save()
            messages.success(request, 'Appointment scheduled!')
        else:
            messages.error(request, 'Failed to schedule appointment.')
        return redirect('/appointment/' + pk)

    data = {
        'patient': patient,
        'appointment_form': appointment_form,
        'appointments': appointments,
        'age': age,
    }

    return render(request, 'patientmonitoring/appointment.html', data)


@login_required(login_url='login')
def editAppointment(request, pk):
    patient = Patient.objects.get(id=pk)
    #edit_appointment_form = EditAppointmentForm(instance=patient)

    appointments = Appointment.objects.all()

    # -- Age (X Years Y Months) --
    curr_date = datetime.date.today()
    months = curr_date.month - patient.birthdate.month
    years = curr_date.year - patient.birthdate.year
    age = "{} year {} month".format(years, months)

    if (request.method == "GET"):
        edit_appointment_form = EditAppointmentForm(instance=patient)
    else:
        edit_appointment_form = EditAppointmentForm(request.POST, instance=patient)
        if edit_appointment_form.is_valid():
            edit_appointment_form.save()

        return redirect('/appointment/' + pk)

    # if(request.method == "POST"):
    #     edit_appointment_form = EditAppointmentForm(request.POST, instance=patient)
    #     if edit_appointment_form.is_valid():
    #         edit_appointment_form.save()
       
    #     return redirect('/appointment/' + pk)

    data = {
        'patient': patient,
        'edit_appointment_form': edit_appointment_form,
        'appointments': appointments,
        'age': age,
    }
    return render(request, 'patientmonitoring/editAppointment.html', data)


@login_required(login_url='login')
def portal(request, pk):
    patient = Patient.objects.get(id=pk)
    portal_form = PortalForm()
    patient_form = PatientUserForm()
    
    # -- Age (X Years Y Months) --
    curr_date = datetime.date.today()
    months = curr_date.month - patient.birthdate.month
    years = curr_date.year - patient.birthdate.year
    age = "{} year {} month".format(years, months)

    if request.method == 'POST':
        portal_form = PortalForm(request.POST)
        patient_form = PatientUserForm(request.POST)
        if portal_form.is_valid() and patient_form.is_valid():
            user = portal_form.save()
            profile = patient_form.save(commit=False)
            profile.user = user
            profile.patient = patient
            profile.save()
            messages.success(request, 'Account Created!')
        else:
            messages.error(request, 'Failed to create account.')
        return redirect('/portal/' + pk)
    
    data = {
        'patient': patient, 
        'age': age,
        'portal_form': portal_form,
        'patient_form': patient_form,
    }
    return render(request, 'patientmonitoring/portal.html', data)

@login_required(login_url='login')
def certificate(request, pk):
    patient = Patient.objects.get(id=pk)
    cert_date_form = CertDateForm(instance=patient)
    #cert_date = None

    # -- Age (x Years y Months) -- 
    curr_date = datetime.date.today()
    months = curr_date.month - patient.birthdate.month
    years = curr_date.year - patient.birthdate.year
    age = "{} year {} month".format(years, months)

    if(request.method == "POST"):
         cert_date_form = EditAppointmentForm(request.POST, instance=patient)
         if cert_date_form.is_valid():
             cert_date_form.save()
       
         return redirect('/certificate/' + pk)

    # if(request.method == "POST"):
    #     cert_date = request.POST.get['sign_cert']

    # if cert_date:
    #     if patient:
    #         patient.cert_date = cert_date
    #         patient.save()
    #     return redirect('/certificate/' + pk)

    data = {
        'patient': patient, 
        'age': age,
        'curr_date': curr_date,
        'cert_date_form': cert_date_form,
    }
    return render(request, 'patientmonitoring/certificate.html', data)

class PdfDetail(PDFTemplateResponseMixin, DetailView):
    template_name = 'patientmonitoring/pdf_cert.html'
    model = Patient
    download_filename = 'Vaccine Certificate of {}-{}'.format(model.last_name, model.first_name)
    context_object_name = 'patient'

    # def get_context_data(self, request, pk, **kwargs):
    #     return super(PdfDetail, self).get_context_data(
    #         model = Patient,
    #         download_filename = 'Vaccine Certificate of {}-{}'.format(model.last_name, model.first_name),
    #         context_object_name = 'patient',
    #         # -- Age (x Years y Months) -- 
    #         curr_date = datetime.date.today(),
    #         months = curr_date.month - patient.birthdate.month,
    #         years = curr_date.year - patient.birthdate.year,
    #         age = "{} year {} month".format(years, months)
    #     )
        

@login_required(login_url='login')
def vaccine(request, pk):
    patient = Patient.objects.get(id=pk)
    #vaccines = PatientVaccine.objects.all()

    # -- Age (X Years Y Months) --
    curr_date = datetime.date.today()
    months = curr_date.month - patient.birthdate.month
    years = curr_date.year - patient.birthdate.year
    age = "{} year {} month".format(years, months)
    
    data = {
        'patient': patient, 
        #'vaccines': vaccines,
        'age': age,
    }
    return render(request, 'patientmonitoring/vaccine.html', data)

@login_required(login_url='login')
def editVaccine(request, pk):
    patient = Patient.objects.get(id=pk)
    # vaccine_form = PatientVaccineForm(initial={'patient': patient})
    # vaccines = PatientVaccine.objects.all()
    vaccine_form = PatientVaccineForm(instance=patient)

    # -- Age (X Years Y Months) --
    curr_date = datetime.date.today()
    months = curr_date.month - patient.birthdate.month
    years = curr_date.year - patient.birthdate.year
    age = "{} year {} month".format(years, months)

    if(request.method == "POST"):
        vaccine_form = PatientVaccineForm(request.POST, instance=patient)
        if vaccine_form.is_valid():
            vaccine_form.save()
       
        return redirect('/vaccine/' + pk)
    
    data = {
        'patient': patient, 
        'vaccine_form': vaccine_form,
        #'vaccines': vaccines,
        'age': age,
    }
    return render(request, 'patientmonitoring/editVaccine.html', data)

