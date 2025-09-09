from django.urls import path
from . import views

urlpatterns = [
    path('', views.set_budget, name='set_budget'),
    path('budget/<int:budget_id>/', views.budget_detail, name='budget_detail'),
]
