from django.urls import path

from .views import (ScheduleListView, ScheduleCreateView,
                    CreateViewFinalSchedule, InstructorScheduleListView,
                    CourseDetailView, ScheduleUpdateView,
                    FinalScheduleUpdateView, ScheduleDeleteView,
                    FinalScheduleDetailView, FinalScheduleDeleteView)

urlpatterns = [
    path('', ScheduleListView.as_view(), name='home'),
    path('create_schedule/', ScheduleCreateView.as_view(), name='create'),
    path('<int:pk>/', CourseDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', ScheduleUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ScheduleDeleteView.as_view(), name='delete'),
    path('final_schedule/', CreateViewFinalSchedule.as_view(), name='final'),
    path('final_schedule/<int:pk>/', FinalScheduleDetailView.as_view(), name='final-detail'),
    path('final_schedule/update/<int:pk>/', FinalScheduleUpdateView.as_view(), name='final-update'),
    path('final_schedule/<int:pk>/delete/', FinalScheduleDeleteView.as_view(), name='final-delete'),
    path('<str:user>/', InstructorScheduleListView.as_view(), name='instructor'),

]
