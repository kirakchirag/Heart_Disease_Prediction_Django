from django.shortcuts import render, redirect
import pandas as pd
from .models import PatientInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')

        else:
            messages.error(request, 'Check your Username or Password!')
            return render(request, 'index.html')

    return render(request, 'index.html')


def dashboard(request):
    if request.user.is_anonymous:
        return redirect('/')

    return render(request, 'dashboard.html')


def module1(request):
    if request.method == "POST":
        Age = request.POST.get('age')
        sex = request.POST.get('sex')
        if sex == "Female (0)":
            Sex = 0
        else:
            Sex = 1
        ChestPain = request.POST.get('chest_pain')
        if ChestPain == 'Typical Angina (1)':
            Chest_Pain = 1
        elif ChestPain == 'Atypical Angina (2)':
            Chest_Pain = 2
        elif ChestPain == 'Non-Anginal Pain (3)':
            Chest_Pain = 3
        elif ChestPain == 'Asymptomatic (4)':
            Chest_Pain = 4
        Rest_BP = request.POST.get('rest_bp')
        Cholestrol = request.POST.get('cholestrol')
        FastBS = request.POST.get('fast_bs')
        if FastBS == "False (0)":
            Fast_BS = 0
        else:
            Fast_BS = 1

        RestECG = request.POST.get('rest_ecg')
        if RestECG == "Normal (0)":
            Rest_ECG = 0
        elif RestECG == "Abnormal (1)":
            Rest_ECG = 1
        else:
            Rest_ECG = 2
        Max_Heart_Rate = request.POST.get('maximun_heart_rate')
        exercise = request.POST.get('exercise')
        if exercise == "Yes (1)":
            Exercise = 1
        else:
            Exercise = 0

        ExertoRest = request.POST.get('exertorest')

        slope = request.POST.get('slope')
        if slope == "Up (1)":
            Slope = 1
        elif slope == "Down (3)":
            Slope = 3
        else:
            Slope = 2
        No_Major_Vessels = request.POST.get('no_of_major_vessels')
        thal = request.POST.get('thal')
        if thal == "Normal (3)":
            Thal = 3
        elif thal == "Fixed (6)":
            Thal = 6
        else:
            Thal = 7

        model = pd.read_pickle(r"random_forest.pickle")
        result = model.predict([[Age, Sex, Chest_Pain, Rest_BP, Cholestrol, Fast_BS,
                                 Rest_ECG, Max_Heart_Rate, Exercise, ExertoRest, Slope, No_Major_Vessels, Thal]])

        Heart_Disease = result[0]
        if Heart_Disease == 0:
            Heart_Disease = "No-Disease"
        else:
            Heart_Disease = "Heart Disease"

        Pent = PatientInfo(Age=Age, Sex=sex, Chest_Pain=ChestPain, Rest_BP=Rest_BP, Cholestrol=Cholestrol, Fast_BS=FastBS, Rest_ECG=RestECG, Max_Heart_Rate=Max_Heart_Rate,
                           Exercise=exercise, ExertoRest=ExertoRest, Slope=slope, No_Major_Vessels=No_Major_Vessels, Thal=thal, Heart_Disease=Heart_Disease)
        Pent.save()
        context = {'result': Heart_Disease}

        return render(request, 'module1.html', context)

    return render(request, 'module1.html')


def module2(request):
    if request.method == "POST":
        Age = request.POST.get('age')
        sex = request.POST.get('sex')
        if sex == "Female (0)":
            Sex = 0
        else:
            Sex = 1
        ChestPain = request.POST.get('chest_pain')
        if ChestPain == 'Typical Angina (1)':
            Chest_Pain = 1
        elif ChestPain == 'Atypical Angina (2)':
            Chest_Pain = 2
        elif ChestPain == 'Non-Anginal Pain (3)':
            Chest_Pain = 3
        elif ChestPain == 'Asymptomatic (4)':
            Chest_Pain = 4
        Rest_BP = request.POST.get('rest_bp')
        Cholestrol = request.POST.get('cholestrol')
        FastBS = request.POST.get('fast_bs')
        if FastBS == "False (0)":
            Fast_BS = 0
        else:
            Fast_BS = 1

        RestECG = request.POST.get('rest_ecg')
        if RestECG == "Normal (0)":
            Rest_ECG = 0
        elif RestECG == "Abnormal (1)":
            Rest_ECG = 1
        else:
            Rest_ECG = 2
        Max_Heart_Rate = request.POST.get('maximun_heart_rate')
        exercise = request.POST.get('exercise')
        if exercise == "Yes (1)":
            Exercise = 1
        else:
            Exercise = 0

        ExertoRest = request.POST.get('exertorest')

        slope = request.POST.get('slope')
        if slope == "Up (1)":
            Slope = 1
        elif slope == "Down (3)":
            Slope = 3
        else:
            Slope = 2
        No_Major_Vessels = request.POST.get('no_of_major_vessels')
        thal = request.POST.get('thal')
        if thal == "Normal (3)":
            Thal = 3
        elif thal == "Fixed (6)":
            Thal = 6
        else:
            Thal = 7

        model = pd.read_pickle(r"random_forest.pickle")

        result = model.predict([[Age, Sex, Chest_Pain, Rest_BP, Cholestrol, Fast_BS,
                                 Rest_ECG, Max_Heart_Rate, Exercise, ExertoRest, Slope, No_Major_Vessels, Thal]])

        Heart_Disease = result[0]
        if Heart_Disease == 0:
            Heart_Disease = "No-Disease"
        elif Heart_Disease == 1:
            Heart_Disease = "Type 1(Heart Disease)"
        elif Heart_Disease == 2:
            Heart_Disease = "Type 2(Heart Disease)"
        elif Heart_Disease == 3:
            Heart_Disease = "Type 3(Heart Disease)"
        else:
            Heart_Disease = "Type 4(Heart Disease)"

        Pent = PatientInfo(Age=Age, Sex=sex, Chest_Pain=ChestPain, Rest_BP=Rest_BP, Cholestrol=Cholestrol, Fast_BS=FastBS, Rest_ECG=RestECG, Max_Heart_Rate=Max_Heart_Rate,
                           Exercise=exercise, ExertoRest=ExertoRest, Slope=slope, No_Major_Vessels=No_Major_Vessels, Thal=thal, Heart_Disease=Heart_Disease)
        Pent.save()
        context = {'result': Heart_Disease}

        return render(request, 'module2.html', context)

    return render(request, 'module2.html')


def module3(request):
    if request.method == "POST":
        Age = request.POST.get('age')
        sex = request.POST.get('sex')
        if sex == "Female (0)":
            Sex = 0
        else:
            Sex = 1
        ChestPain = request.POST.get('chest_pain')
        if ChestPain == 'Typical Angina (1)':
            Chest_Pain = 1
        elif ChestPain == 'Atypical Angina (2)':
            Chest_Pain = 2
        elif ChestPain == 'Non-Anginal Pain (3)':
            Chest_Pain = 3
        elif ChestPain == 'Asymptomatic (4)':
            Chest_Pain = 4
        Rest_BP = request.POST.get('rest_bp')
        Cholestrol = request.POST.get('cholestrol')
        FastBS = request.POST.get('fast_bs')
        if FastBS == "False (0)":
            Fast_BS = 0
        else:
            Fast_BS = 1

        RestECG = request.POST.get('rest_ecg')
        if RestECG == "Normal (0)":
            Rest_ECG = 0
        elif RestECG == "Abnormal (1)":
            Rest_ECG = 1
        else:
            Rest_ECG = 2
        Max_Heart_Rate = request.POST.get('maximun_heart_rate')
        exercise = request.POST.get('exercise')
        if exercise == "Yes (1)":
            Exercise = 1
        else:
            Exercise = 0

        ExertoRest = request.POST.get('exertorest')

        slope = request.POST.get('slope')
        if slope == "Up (1)":
            Slope = 1
        elif slope == "Down (3)":
            Slope = 3
        else:
            Slope = 2
        No_Major_Vessels = request.POST.get('no_of_major_vessels')
        thal = request.POST.get('thal')
        if thal == "Normal (3)":
            Thal = 3
        elif thal == "Fixed (6)":
            Thal = 6
        else:
            Thal = 7

        model = pd.read_pickle(r"random_forest.pickle")
        result = model.predict([[Age, Sex, Chest_Pain, Rest_BP, Cholestrol, Fast_BS,
                                 Rest_ECG, Max_Heart_Rate, Exercise, ExertoRest, Slope, No_Major_Vessels, Thal]])

        Heart_Disease = result[0]
        if Heart_Disease == 0:
            Heart_Disease = "No-Disease"
        else:
            Heart_Disease = "Heart Disease"

        Pent = PatientInfo(Age=Age, Sex=sex, Chest_Pain=ChestPain, Rest_BP=Rest_BP, Cholestrol=Cholestrol, Fast_BS=FastBS, Rest_ECG=RestECG, Max_Heart_Rate=Max_Heart_Rate,
                           Exercise=exercise, ExertoRest=ExertoRest, Slope=slope, No_Major_Vessels=No_Major_Vessels, Thal=thal, Heart_Disease=Heart_Disease)
        Pent.save()
        context = {'result': Heart_Disease}

        return render(request, 'module3.html', context)

    return render(request, 'module3.html')


def view_results(request):

    data = {"dataset": PatientInfo.objects.all()}

    return render(request, "results.html", data)


def log_out(request):
    logout(request)
    return redirect('/')
