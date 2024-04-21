from django import forms
from .models import ResumeData

GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female')
]
JOB_CHOICES=[
    ('Noida','Noida 62'),
    ('Delhi','Delhi'),
    ('Gurugram','Gurugram'),
    ('Patna','Patna')
]

class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect(attrs={'class':'d-inline-flex'}))
    job_city=forms.MultipleChoiceField(label='Preferred Job Locations',choices=JOB_CHOICES,widget=forms.CheckboxSelectMultiple(attrs={'class':'d-inline-flex'}))
    class Meta:
        model=ResumeData
        fields='__all__'
        labels={
            'name':'Full Name',
            'dob':'Data of Birth',
            'mobile_num':'Mobile No.',
            'profile_img':'Profile Image',
            'my_file':'Resume',
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'pin_code':forms.NumberInput(attrs={'class':'form-control'}),
            'mobile_num':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}), 
        }