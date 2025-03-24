from django.shortcuts import render, redirect
from .forms import RegistrationStep1Form, RegistrationStep2Form, RegistrationStep3Form
from django.http import HttpResponse

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
