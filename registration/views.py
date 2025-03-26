from django.shortcuts import render, redirect
from .forms import RegistrationStep1Form, RegistrationStep2Form, RegistrationStep3Form
from django.http import HttpResponse
from .models import User, RegistrationStep1, RegistrationStep2


def registration_step1(request):
    form = RegistrationStep1Form()
    if request.method == 'POST':
        form = RegistrationStep1Form(request.POST)
        if form.is_valid():
            # Traitez le formulaire valide
            form.save()
            return redirect('registration_step2') # Redirige vers step2 après la sauvegarde
    return render(request, 'registration/step1.html', {'form': form}) 

def registration_step2(request):
    if request.method == 'POST':
        form = RegistrationStep2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_step3')  # Redirect to step 3
    else:
        form = RegistrationStep2Form()
    return render(request, 'registration/step2.html', {'form': form})

def registration_step3(request):
    if request.method == 'POST':
        form = RegistrationStep3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_thankyou')  # Redirect to thankyou page
    else:
        form = RegistrationStep3Form()
    return render(request, 'registration/step3.html', {'form': form})

def registration_thankyou(request):
    return render(request, 'registration/thankyou.html')


def registration_step1(request):
    if request.method == 'POST':
        form = RegistrationStep1Form(request.POST)
        if form.is_valid():
            step1 = form.save()
            request.session['step1_id'] = step1.id
            return redirect('registration_step2')
    else:
        form = RegistrationStep1Form()
    return render(request, 'registration/step1.html', {'form': form})

def registration_step2(request):
    if request.method == 'POST':
        form = RegistrationStep2Form(request.POST)
        if form.is_valid():
            step2 = form.save()
            request.session['step2_id'] = step2.id
            return redirect('registration_step3')
    else:
        form = RegistrationStep2Form()
    return render(request, 'registration/step2.html', {'form': form})

def registration_step3(request):
    if request.method == 'POST':
        form = RegistrationStep3Form(request.POST)
        if form.is_valid():
            step3 = form.save()
            step1 = RegistrationStep1.objects.get(id=request.session['step1_id'])
            step2 = RegistrationStep2.objects.get(id=request.session['step2_id'])
            User.objects.create(
                full_name=step1.full_name,
                email=step1.email,
                password=step1.password,
                phone_number=step1.phone_number,
                city=step1.city,
                terms_accepted=step1.terms_accepted,
                project_name=step2.project_name,
                project_level=step2.project_level,
                description=step2.description,
                industry=step2.industry,
                choice=step3.choice,
            )
            return redirect('registration_thankyou')
    else:
        form = RegistrationStep3Form()
    return render(request, 'registration/step3.html', {'form': form})

def registration_thankyou(request):
    return render(request, 'registration/thankyou.html')
