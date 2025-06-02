from django.urls import path
from myapp import views

urlpatterns = [
    path('myapi/', views.api_list), # type: ignore
    path('myapi/<int:pk>/', views.api_detail), # type: ignore
]