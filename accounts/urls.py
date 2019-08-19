from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('signup/student/', views.register_student, name='student'),
    path('signup/instructor/', views.register_instructor, name='instructor'),
    path('signup/coordinator/', views.register_coordinator, name='coordinator'),
    path('login/student/', LoginView.as_view(template_name='accounts/login_student.html'), name='login-student'),
    path('login/instructor/', LoginView.as_view(template_name='accounts/login_instructor.html'), name='login-instructor'),
    path('login/coordinator/', LoginView.as_view(template_name='accounts/login_coordinator.html'), name='login-coordinator'),
]
