from django import forms
from .models import Student,Course
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'courses']
    
    def __init__(self, *args, **kwargs):
        super(StudentProfileForm, self).__init__(*args, **kwargs)
        self.fields['courses'].widget = forms.CheckboxSelectMultiple()
        self.fields['courses'].help_text = "Select the courses you want to enroll in"
        #readonly
        self.fields['student_id'].widget.attrs['readonly'] = True
class StaffRegistrationForms(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address")
    first_name = forms.CharField(max_length=30,required=True,help_text="Enter your first name")
    last_name = forms.CharField(max_length=30,required=True,help_text='Enter your last name')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'code', 'credits']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'credits': forms.NumberInput(attrs={'class': 'form-control'}),
        }
