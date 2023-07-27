from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('events/', views.EventList.as_view(), name='event_list'),
    path('events/<int:pk>', views.EventDetail.as_view(), name='event_detail'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('expenses/', views.ExpenseList.as_view(), name='expense_list'),
    path('expenses/<int:pk>', views.ExpenseDetail.as_view, name='expense_detail'),
    path('attendees/', views.AttendeeList.as_view(), name='attendee_list'),
    path('attendees/<int:pk>', views.AttendeeDetail.as_view(), name='attendee_detail'),
    path('tasks/', views.TaskList.as_view(), name='task_list'),
    path('tasks/<int:pk>', views.TaskDetail.as_view(), name='task_detail'),
]