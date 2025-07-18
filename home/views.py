from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import jwt
from datetime import datetime, timedelta

# Helper function to generate the Intercom JWT
def generate_intercom_token(user):
    """
    Generates an Intercom User Identity Verification JWT for a given user.
    """
    if not user.is_authenticated:
        # Or handle this case based on your needs, e.g., return None
        return None

    # Intercom recommends a short expiry for security, e.g., 1 hour
    expires_at = int((datetime.utcnow() + timedelta(hours=1)).timestamp())

    # Payload must include 'user_id'
    payload = {
        'user_id': str(user.id), # Use user.id (which is unique)
        'email': user.email,     # Optional, but highly recommended if available
        # You can add other sensitive attributes here if needed for Intercom
        # 'sensitive_attribute1': 'some_data',
        'exp': expires_at
    }

    # Use your API secret from settings
    token = jwt.encode(payload, settings.INTERCOM_API_SECRET, algorithm='HS256')
    return token

@login_required
def home_with_intercom(request):
    """
    A view that generates the Intercom token and passes it to the template.
    This view requires the user to be logged in.
    """
    intercom_user_jwt = generate_intercom_token(request.user)
    context = {
        'intercom_app_id': settings.INTERCOM_APP_ID,
        'intercom_user_jwt': intercom_user_jwt,
    }
    return render(request, 'home_with_intercom.html', context)

def index(request):
    return render(request, 'index.html', {'data': 'some_data'})