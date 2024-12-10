from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('read_more/', views.read_more, name='read_more'),
    path('join_now/', views.join_now, name='join_now'),

    path('explore/', views.explore, name='explore'),
    path('explore/<int:course_id>/', views.explored, name='explore'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('sign_up<int:course_id>/', views.sign_up_view, name='sign_up'),
    path('courses/', views.courses, name='courses'),  # View for listing all courses
    path('courses/<int:course_id>/', views.course, name='course'),  # Detail view for a specific course
    path('courses/', views.course_view, name='course'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('faqs_and_help/', views.faqs_and_help, name='faqs_and_help'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]