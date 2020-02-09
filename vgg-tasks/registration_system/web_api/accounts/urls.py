from django.urls import path
from accounts import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('projects/',views.projectList.as_view(),name="project_url"),
    path('projects/<int:id>/',views.project_view.as_view(),name="project_url"),
    path('users/', views.user_view.as_view(), name="users_url"),
    path('actions/', views.action_view.as_view(), name="action_url"),
    path('actions/<int:id>/', views.action_view.as_view(), name="action_url"),
    
]