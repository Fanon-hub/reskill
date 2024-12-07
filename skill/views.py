from urllib import request

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Course
from .forms import CourseForm


#Home page view
def home(request):
    return render(request, 'skills/index.html', {'title': 'Home'})

# Courses listing view
def courses(request):
    # Mock data for demonstration purposes
    courses_list = [
        {'id': 1, 'name': 'Introduction to Python', 'description': 'Learn the basics of Python programming.'},
        {'id': 2, 'name': 'Web Development with Django', 'description': 'Build web applications using Django.'},
        {'id': 3, 'name': 'Frontend Development', 'description': 'Master HTML, CSS, and JavaScript.'},
    ]
    return render(request, 'skills/courses.html', {'title': 'Courses', 'courses': courses_list})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return HttpResponse('Thank you for contacting us!')
    return render(request, 'skills/contact.html', {'title': 'Contact'})

# Course detail view
def course_detail(request, course_id):
    # Mock data for demonstration purposes
    courses_detail = {
        1: {'name': 'Machine Learning', 'description': 'Machine Learning and Deep Learning'},
        2: {'name': 'Introduction to Python', 'description': 'Learn the basics of Python programming.'},
        3: {'name': 'Digital Marketing', 'description': 'Digital Marketing'},
        4: {'name': 'Web Development ', 'description': 'Build web applications using Django.'},
        5: {'name': 'Graphics Design', 'description': 'Master art in creating dynamic designs on various websites.'},

    }
    course = courses_detail.get(course_id, None)
    if not course:
        return HttpResponse('Course not found', status=404)
    return render(request, 'skills/course_detail.html', {'title': course['name'], 'course': course})

# About page view
def about(request):
    return render(request, 'skills/about.html', {'title': 'About'})

def course(request):
    courses_list = Course.objects.all()
    return render(request, 'skills/courses.html', {'title': 'Courses', 'courses': courses_list})

def read_more(request):
    return render(request, 'skills/read_more.html')
def join_now(request):
    return render(request, 'skills/join_now.html')

# Create
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'programmes/create_course.html', {'form': form})

# Read
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'programmes/course_list.html', {'courses': courses})

def course_info(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'programmes/course_info.html', {'course': course})

# Update
def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'programmes/update_course.html', {'form': form})

# Delete
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'programmes/delete_course.html', {'course': course})
def privacy_policy(request):
    return render(request, 'privacy_policy.html')
def terms_and_conditions(request):
    return render(request, 'terms_and_conditions.html')
def faqs_and_help(request):
    return render(request, 'faqs_and_help.html')