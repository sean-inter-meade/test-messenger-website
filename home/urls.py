from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('dashboard/', views.home_with_intercom, name='dashboard_intercom'),
]