from django.shortcuts import render
# Create your views here.

def patient_analysis(request):
    return render(request,'analysis.html',{})