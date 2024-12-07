from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in hours")
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

    def _str_(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f" {self.title} ({self.course.name})"

