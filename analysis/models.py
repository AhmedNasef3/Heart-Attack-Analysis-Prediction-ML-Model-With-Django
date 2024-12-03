from django.db import models


SEX_TYPE=(
    (1,'M'),
    (0,'F')
)

EXANG_TYPE=(
    (1,'Yes'),
    (0,'No')
)

CA_TYPE=(
    (0,'Zero'),
    (1,'One'),
    (2,'Two'),
    (3,'Three'),
    (4,'Four')
)

CP_TYPE=(
    (0,'typical angina'),
    (1,'atypical angina'),
    (2,'non-anginal pain'),
    (3,'asymptomatic')
)

FBS_TYPE=(
    (1,'Yes'),
    (0,'No')
)

REST_ECG_TYPE=(
    (0,'normal'),
    (1,'having ST-T wave abnormality'),
    (2,'showing probable or definite left ventricular hypertrophy')
    
)

TARGET_TYPE=(
    (1,'Yes'),
    (0,'No')
)

# Create your models here.

class Patient(models.Model):
    age=models.IntegerField()
    sex=models.CharField(max_length=2,choices=SEX_TYPE)
    exang=models.CharField(max_length=5,choices=EXANG_TYPE,help_text='exercise induced angina')
    ca=models.CharField(max_length=6,choices=CA_TYPE,help_text='number of major vessels')
    cp=models.CharField(max_length=20,choices=CP_TYPE,help_text='Chest Pain type')
    trtbps=models.IntegerField(help_text='resting blood pressure (in mm Hg)')
    chol=models.IntegerField(help_text='cholestoral in mg/dl fetched via BMI sensor')
    fbs=models.CharField(max_length=5,choices=FBS_TYPE,help_text='fasting blood sugar > 120 mg/dl')
    rest_ecg=models.CharField(max_length=65,choices=REST_ECG_TYPE,help_text='resting electrocardiographic results')
    thalach=models.IntegerField(help_text='maximum heart rate achieved')
    target=models.CharField(max_length=5,choices=TARGET_TYPE,null=True,blank=True)

    def __str__(self):
         return f"Patient Age: {self.age}"