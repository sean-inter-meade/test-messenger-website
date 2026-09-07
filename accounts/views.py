from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def update_test_attribute(request):
    if request.method == 'POST':
        request.user.profile.test_attribute = request.POST.get('test_attribute', '')
        request.user.profile.save()
    return redirect('dashboard_intercom')
