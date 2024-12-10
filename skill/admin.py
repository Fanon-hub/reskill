from django.contrib import admin
from .models import Course, Lesson, UserProfile


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'duration', 'created_at')
    search_fields = ('name', 'level')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course','created_at')
    search_fields = ('title', 'course__name')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'role', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('role', 'created_at')


