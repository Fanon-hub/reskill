from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Course,Student, Lesson, Participant, StudentEnrollment, UserProfile
from .forms import CourseForm, SignUpForm


#Home page view
def home(request):
    courses = Course.objects.all()
    return render(request, 'skills/index.html', {'title': 'Home', 'courses': courses})

def courses(request):
    all_courses = Course.objects.all()  # Retrieve all courses
    return render(request, 'skills/courses.html', {'courses': all_courses})
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return HttpResponse('Thank you for contacting us!')
    return render(request, 'skills/contact.html', {'title': 'Contact'})

# Course detail view
def course_detail(request, course_id):
    # Retrieve the course by ID
    course = get_object_or_404(Course, id=course_id)

    # Pass course and its participants to the template
    participants = course.participants.all()  # Assuming a related name "participants"
    return render(request, 'skills/course_detail.html', {
        'course': course,
        'participants': participants
    })


def sign_up_view(request, course_id):
    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Call the save method to create and save the Participant
            form.save(course=course, user=request.user)
            return redirect('course_detail', course_id=course.id)  # Redirect to course detail page
    else:
        form = SignUpForm()

    return render(request, 'skills/sign_up.html', {'form': form, 'course': course})


# About page view
def about(request):
    return render(request, 'skills/about.html', {'title': 'About'})

# def course(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     return render(request, 'skills/courses.html', {'title': 'Courses', 'course': course})

def course(request, course_id):
    course = get_object_or_404(Course, id=course_id)  # Get course by ID or return 404
    return render(request, 'skills/course_detail.html', {'course': course})

def course_view(request, course_id):
    course = Course.objects.all()  # Get course by ID or return 404
    return render(request, 'skills/course_detail.html', {'course': course})

def read_more(request):
    return render(request, 'skills/read_more.html')
def join_now(request):
    return render(request, 'skills/join_now.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')
def terms_and_conditions(request):
    return render(request, 'terms_and_conditions.html')
def faqs_and_help(request):
    return render(request, 'faqs_and_help.html')

def explore(request):
    courses = Course.objects.all()  # Retrieve all courses (or filter as needed)
    context = {
        'courses': courses,
    }
    return render(request, 'skills/explore.html', context)

def explored(request, course_id):
    courses = get_object_or_404(Course, id=course_id)
    return render(request, 'skills/explore.html', {'course': courses})

