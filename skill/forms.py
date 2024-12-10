from django.contrib.auth.models import User

from .models import Course, Participant
import re
from django import forms
from django.core.exceptions import ValidationError

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=100, label='Full Name',
                           widget=forms.TextInput(attrs={'placeholder': 'Enter your full name', 'required': True}))
    email = forms.EmailField(max_length=100, label='Email Address',
                             widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'required': True}))
    phone = forms.CharField(max_length=15, label='Phone Number', required=False,
                            widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}))

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        # Check if the phone number is provided
        if phone:
            # Regular expression for validating a basic phone number pattern
            phone_regex = re.compile(r'^\+?[\d\s\-\(\)]{7,15}$')

            # If phone number doesn't match the regex, raise a validation error
            if not phone_regex.match(phone):
                raise ValidationError("Enter a valid phone number.")

        return phone

    def save(self, course, user, commit=True):
        """
        This method creates a new Participant and associates it with the provided course and user.
        """
        # Create a new Participant instance
        participant = Participant(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            phone=self.cleaned_data.get('phone', ''),
            course=course,
            user=user
        )

        # Save the participant instance to the database
        if commit:
            participant.save()

        return participant


