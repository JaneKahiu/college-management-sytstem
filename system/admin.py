from django.contrib import admin
from .models import Student, Course, Assignment, AssignmentSubmission, Grade

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(AssignmentSubmission)
admin.site.register(Grade)

