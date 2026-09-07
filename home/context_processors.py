from django.conf import settings
from datetime import datetime, timedelta, timezone
import jwt


def intercom(request):
    context = {
        'intercom_app_id': settings.INTERCOM_APP_ID,
        'intercom_user_jwt': None,
    }
    if request.user.is_authenticated:
        expires_at = int((datetime.now(timezone.utc) + timedelta(hours=1)).timestamp())
        payload = {
            'user_id': str(request.user.id),
            'email': request.user.email,
            'exp': expires_at,
        }
        context['intercom_user_jwt'] = jwt.encode(
            payload, settings.INTERCOM_API_SECRET, algorithm='HS256'
        )
    return context
