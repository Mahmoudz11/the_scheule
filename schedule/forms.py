from django import forms

from .models import Course, FinalSchedule


class CreateSchedule(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'day', 'from_hour', 'to_hour', 'location']

    def clean_hour(self):
        if self.cleaned_data['from_hour'] >= self.cleaned_data['to_hour']:
            raise forms.ValidationError('Course end time must be greater than start time!')
        return self.cleaned_data
