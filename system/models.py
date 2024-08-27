from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    code = models.CharField(max_length=10)
    credits = models.IntegerField()

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10)
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.user.get_full_name()

class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')

    def __str__(self):
        return self.title

class AssignmentSubmission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    submitted_at = models.DateTimeField(auto_now_add=True)
    files = models.FileField(upload_to='assignments/')  # Fixed typo

    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.assignment.title}"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades', default=1)  # Temporarily set default
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='grades')
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.course.name}: {self.score}"
    
