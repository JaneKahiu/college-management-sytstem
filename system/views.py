from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required,user_passes_test
from.models import Course, Student, Assignment, AssignmentSubmission, Grade
from .forms import StudentProfileForm,StaffRegistrationForms,CourseForm
from django.contrib .auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

#home view
def home(request):
    return render(request, 'home.html')
# views for student app
@login_required
def studentdashboard(request):
    student = Student.objects.get(user=request.user)
    courses = student.courses.all()
    assignments = Assignment.objects.filter(course__in=courses).order_by('due_date')
    grades = Grade.objects.filter(student=student)
    
    context = {
        'student': student,
        'courses': courses,
        'assignments': assignments,
        'grades': grades,
    }
    
    return render(request, 'studentdashboard.html', context)
@login_required
def view_courses(request):
  courses = Course.objects.all()
  context = {
    'courses': courses,
  }
  return render(request, 'courses.html', context)
#view course details
@login_required
def view_course_details(request, course_id):
  course = Course.objects.get(id=course_id)
  context = {
    'course': course,
  }
  return render(request, 'course_details.html', context)

#view grades
@login_required
def view_grades(request):
  grades = request.user.student.grades.all()
  context = {'grades': grades}
  return render(request, 'grade.html', context)

#profile management
@login_required
def student_profile(request):
  if request.method == 'POST':
    form = StudentProfileForm(request.POST, instance=request.user.student)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('studentdashboard')
  else:
    form = StudentProfileForm(instance=request.user.student)
  context = {'form':form}
  return render(request, 'studentprofile.html', context)  
#login view

def student_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Extract cleaned data
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student_dashboard')  # Ensure this matches your URL pattern name
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

#registration view
def student_registration(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('studentdashboard')
  else:
      form = UserCreationForm()
  return render(request, 'registration/registration.html', {'form':form})
  
#logout view
def student_logout(request):
  logout(request)
  return redirect('student_login')
    

    
#staff interface views
#staff_login view

def staff_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('staff_dashboard')  # Redirect to staff dashboard
            else:
                # Invalid login or not a staff member
                form.add_error(None, "Invalid credentials or not a staff member.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'staff/login.html', {'form': form})

#staff_registration view
def staff_registration(request):
   if request.method == 'POST':
      form = StaffRegistrationForms(request.POST)
      if form.is_valid():
         user = form.save(commit=False)
         user.is_staff = True
         user.save()
         return redirect('staff_login')
   else:
      form = StaffRegistrationForms()

   return render(request, 'staff/registration.html', {'form': form})

#staff_dashboard view

def is_staff_user(user):
    return user.is_staff

@user_passes_test(is_staff_user)
def staff_dashboard(request):
   return render(request, 'staff/dashboard.html')
#manage course view
@user_passes_test(is_staff_user)
def manage_course(request):
   courses = Course.objects.all()
   return render(request, 'staff/manage_course.html', {'courses': courses})   

 #add course view
@user_passes_test(is_staff_user)
def add_course(request):
   if request.method == 'POST':
      form = CourseForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('manage_course')
   else:
      form = CourseForm()
   return render(request, 'staff/add_course.html', {'form': form})

#update course view
@user_passes_test(is_staff_user)
def update_course(request, course_id):
   course = Course.objects.get(id=course_id)
   if request.method == 'POST':
      form = CourseForm(request.POST, instance=course)
      if form.is_valid():
         form.save()
         return redirect('mangecourse')
   else:
      form = CourseForm(instance=course)
   return render(request, 'staff/update_course.html', {'form': form})

#delete course view
@user_passes_test(is_staff_user)
def delete_course(request, course_id):
   course = Course.objects.get(id=course_id)
   if request.method == 'POST':
      course.delete()
      return redirect('manage_course')
   return render(request, 'staff/delete_course.html', {'course': course})

#staff_logout view
def staff_logout(request):
   logout(request)
   return redirect('staff_login')



           
          
   




    

