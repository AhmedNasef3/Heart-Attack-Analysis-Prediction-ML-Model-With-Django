from django.shortcuts import render
from .forms import PatientForm
# Create your views here.

def patient_analysis(request):
    if request.method=='POST':
         form=PatientForm(request.POST)

         if form.is_valid():
              form.save()
         
         result=model(age=form.cleaned_data['age'])
         if result==0:
              result='not suffer from heartattack'
         else:
              result='suffer from heartattack'
         return render(request,'analysis.html',{'form':form,'result':result})
    form=PatientForm()
    return render(request,'analysis.html',{'form':form})