from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home_with_intercom(request):
    return render(request, 'home_with_intercom.html')


def index(request):
    return render(request, 'index.html')
