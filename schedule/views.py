from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .forms import CreateSchedule
from .models import Course, FinalSchedule


class ScheduleListView(ListView):
    queryset = FinalSchedule.objects.all()


class InstructorScheduleListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Course.objects.filter(instructor_name=self.request.user)


class CourseDetailView(DetailView):
    model = Course


class ScheduleCreateView(CreateView):
    model = Course
    fields = ['course_name', 'day', 'from_hour', 'to_hour', 'location']
    success_url = reverse_lazy('schedule:home')


    def form_valid(self, form):
        # qs = Course.objects.exists(instructor_name=form.instance.instructor_name, day=form.instance.day, from_hour=form.instance.from_hour)
        form.instance.instructor_name = self.request.user
        if form.instance.from_hour >= form.instance.to_hour:
            raise ValidationError('Course end time must be greater than start time!')
        elif Course.objects.filter(instructor_name=form.instance.instructor_name, day=form.instance.day, from_hour=form.instance.from_hour).exists:
            raise ValidationError('You already have a course in this time')

        return super(ScheduleCreateView, self).form_valid(form)

class ScheduleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    fields = ['course_name', 'day', 'from_hour', 'to_hour', 'location']
    success_url = reverse_lazy('schedule:home')


    def form_valid(self, form):
        form.instance.instructor_name = self.request.user
        # qs = Course.objects.get(instructor_name=form.instance.instructor_name, day=form.instance.day, from_hour=form.instance.from_hour)
        if form.instance.from_hour >= form.instance.to_hour:
            raise ValidationError('Course end time must be greater than start time!')
        # elif qs.pk != form.instance.pk :
            # raise ValidationError('You already have a course in this time')
        return super(ScheduleUpdateView, self).form_valid(form)

    def test_func(self):
        schedule = self.get_object()
        if self.request.user == schedule.instructor_name:
            return True
        return False


class ScheduleDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('schedule:home')


class CreateViewFinalSchedule(LoginRequiredMixin, CreateView):
    model = FinalSchedule
    fields = ['schedule']
    success_url = reverse_lazy('schedule:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateViewFinalSchedule, self).form_valid(form)

class FinalScheduleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = FinalSchedule
    fields = ['schedule']
    success_url = reverse_lazy('schedule:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FinalScheduleUpdateView, self).form_valid(form)

    def test_func(self):
        final_schedule = self.get_object()
        if self.request.user == final_schedule.user:
            return True
        return False

class FinalScheduleDeleteView(DeleteView):
    model = FinalSchedule
    success_url = reverse_lazy('schedule:home')


class FinalScheduleDetailView(DetailView):
    model = FinalSchedule
