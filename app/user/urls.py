"""
URl mappings for the user API
"""
from django.urls import URLPattern, path
from user import views


app_name='user'

urlpatters = [
    path('create/', views.CreateUserView.as_view)
]
