from django.urls import path
from . import views

urlpatterns = [
    path("accounts/register/", views.register, name="register"),
    path("accounts/update-test-attribute/", views.update_test_attribute, name="update_test_attribute"),
]
