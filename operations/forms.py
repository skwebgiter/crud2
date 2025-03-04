from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control p-3 bg-dark text-light fs-5 ph-clr','placeholder':'Name'}))
    age = forms.DecimalField(max_digits=2,min_value=0, decimal_places=0 ,widget=forms.NumberInput(attrs={'class':'form-control p-3 bg-dark text-light fs-5 ph-clr','placeholder':'Age'}))
    city = forms.CharField(max_length=10 ,widget=forms.TextInput(attrs={'class':'form-control p-3 bg-dark text-light fs-5 ph-clr','placeholder':'City'}))

    class Meta:
        model = Employee
        fields = ['name','age','city']

