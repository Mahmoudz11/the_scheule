from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegisterStudent, RegisterInstructor, RegisterCoordinator


def register_student(request):
    if request.method == 'POST':
        s_form = RegisterStudent(request.POST)

        if s_form.is_valid():
            s_form.save()
            messages.success(request, f'{request.user.username} account created.')
            return redirect('schedule:home')
    else:
        s_form = RegisterStudent()
    return render(request, 'accounts/register_student.html', {'s_form':s_form})

def register_instructor(request):
    if request.method == 'POST':
        i_form = RegisterInstructor(request.POST)

        if i_form.is_valid():
            i_form.save()
            messages.success(request, f'{request.user.username} account created.')
            return redirect('schedule:home')
    else:
        i_form = RegisterInstructor()
    return render(request, 'accounts/register_instructor.html', {'i_form':i_form})

def register_coordinator(request):
    if request.method == 'POST':
        c_form = RegisterCoordinator(request.POST)

        if c_form.is_valid():
            c_form.save()
            messages.success(request, f'{request.user.username} account created.')
            return redirect('schedule:home')
    else:
        c_form = RegisterCoordinator()
    return render(request, 'accounts/register_coordinator.html', {'c_form':c_form})
