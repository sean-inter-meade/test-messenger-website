from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("update-test-attribute/", views.update_test_attribute, name="update_test_attribute"),
]
