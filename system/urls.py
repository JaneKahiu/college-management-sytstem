from django .urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('studentdashboard', views.studentdashboard, name= 'studentdashboard'),
    path('accouts/student_login', views.student_login, name='student_login'),
    path('student_registration', views.student_registration, name='student_registration'),
    path('student_logout', views.student_logout, name='student_logout'),
    path('student_profile', views.student_profile, name='student_profile'),
    path('view_courses', views.view_courses, name='view_courses'),
    path('view_grades', views.view_grades, name='view_grades'),
    path('view_course_details/<int:course_id>/', views.view_course_details, name='view_course_details'),
    path('staff_dashboard', views.staff_dashboard, name='staff_dashboard'),
    path('staff_login', views.staff_login, name='staff_login'),
    path('staff_registration', views.staff_registration, name='staff_registration'),
    path('staff_logout', views.staff_logout, name='staff_logout'),
    path('manage_course', views.manage_course, name='manage_courses'),
    path('add_course', views.add_course, name='add_course'),
    path('update_course/<int:course_id>/', views.update_course, name='update_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
]