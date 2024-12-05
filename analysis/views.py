from django.shortcuts import render
from .forms import PatientForm
import pickle
# Create your views here.

def patient_analysis(request):
    model=pickle.load(open('final_model.sav','rb'))
    if request.method=='POST':
         form=PatientForm(request.POST)

         if form.is_valid():
              form.save()
              
              age=form.cleaned_data['age']
              sex=form.cleaned_data['sex']
              exang=form.cleaned_data['exang']
              ca=form.cleaned_data['ca']
              cp=form.cleaned_data['cp']
              trtbps=form.cleaned_data['trtbps']
              chol=form.cleaned_data['chol']
              fbs=form.cleaned_data['fbs']
              rest_ecg=form.cleaned_data['rest_ecg']
              thalach=form.cleaned_data['thalach']
              oldpeak=form.cleaned_data['oldpeak']
              thall=form.cleaned_data['thall']
              slp=form.cleaned_data['slp']

              if sex==1:
                   sex_1=1
              else:
                   sex_1=0

              
              if exang==1:
                   exng_1=1
              else:
                   exng_1=0

               
              if ca==0:
                   caa_1=0
                   caa_2=0
                   caa_3=0
                   caa_4=0
              elif ca==1:
                   caa_1=1
                   caa_2=0
                   caa_3=0
                   caa_4=0
              elif ca==2:
                   caa_1=0
                   caa_2=1
                   caa_3=0
                   caa_4=0
              elif ca==3:
                   caa_1=0
                   caa_2=0
                   caa_3=1
                   caa_4=0
              else:
                   caa_1=0
                   caa_2=0
                   caa_3=0
                   caa_4=1

               

              
              if cp==0:
                   cp_1=0
                   cp_2=0
                   cp_3=0
              elif cp==1:
                   cp_1=1
                   cp_2=0
                   cp_3=0
              elif cp==2:
                   cp_1=0
                   cp_2=1
                   cp_3=0
              else:
                   cp_1=0
                   cp_2=0
                   cp_3=1
               
              if fbs==1:
                   fbs_1=1
              else:
                   fbs_1=0

              if rest_ecg==0:
                   restecg_1=0
                   restecg_2=0
              elif rest_ecg==1:
                   restecg_1=1
                   restecg_2=0
              else:
                   restecg_1=0
                   restecg_2=1

              if thall==0:
                   thall_1=0
                   thall_2=0
                   thall_3=0
              elif thall==1:
                   thall_1=1
                   thall_2=0
                   thall_3=0
              elif thall==2:
                   thall_1=0
                   thall_2=1
                   thall_3=0
              else:
                   thall_1=0
                   thall_2=0
                   thall_3=1
                   

              if slp==0:
                   slp_1=0
                   slp_2=0
              elif slp==1:
                   slp_1=1
                   slp_2=0
              else:
                   slp_1=0
                   slp_2=1
              
              result=model.predict([[int(age),trtbps,chol,thalach,oldpeak,sex_1,cp_1,cp_2,cp_3,fbs_1,restecg_1,restecg_2,exng_1,slp_1,slp_2,caa_1,caa_2,caa_3,caa_4,thall_1,thall_2,thall_3]])
              return render(request,'analysis.html',{'form':form,'result':result})
     
    else:
      form=PatientForm()
      return render(request,'analysis.html',{'form':form})
              
         