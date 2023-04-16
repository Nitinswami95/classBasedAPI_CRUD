from django.urls import path
from .views import StudentView, StudentUpdateView

urlpatterns = [
    path('student/', StudentView.as_view()),
    path('student/<int:pk>', StudentUpdateView.as_view())
]