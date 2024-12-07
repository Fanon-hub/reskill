from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.course, name='courses'),
    path('contact/', views.contact, name='contact'),
    path('read_more/', views.read_more, name='read_more'),
    path('join_now/', views.join_now, name='join_now'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses/new/', views.create_course, name='create_course'),
    path('courses/<int:pk>/edit/', views.update_course, name='update_course'),
    path('courses/<int:pk>/delete/', views.delete_course, name='delete_course'),
    path('courses/<int:course_id>/', views.course, name='course'),
    path('course_detail/', views.course_detail, name='courses_detail'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('faqs_and_help/', views.faqs_and_help, name='faqs_and_help'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]