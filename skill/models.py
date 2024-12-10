from django.db import models
from django.contrib.auth.models import User


#
# class Image(models.Model):
    # image=models.ImageField(upload_to='images/', null=True, blank=True)



class Course(models.Model):
    name = models.CharField(max_length=20)
    short_description = models.CharField(max_length=200,default="100")
    course_image = models.ImageField(upload_to="images/", null=True, blank=True)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in months")
    instructor = models.CharField(max_length=100, default="Admin")
    level = models.CharField(
        max_length=50,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced')
        ],
        default='beginner'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_participants(self):
        return self.participants.all()

class Participant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.ForeignKey(Course, related_name="participants", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)



class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f" {self.title} ({self.course.name})"

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('instructor', 'Instructor'),
        ('learner', 'Learner'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Add more fields as necessary

    def _str_(self):
        return self.name


class StudentEnrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('dropped', 'Dropped'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def _str_(self):
        return f"{self.student.name} - {self.course.name}"