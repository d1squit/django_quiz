from django.conf import settings
from django.template.loader import render_to_string

from .models import Result


def send_user_report(user):
    count = len(Result.objects.filter(user_id=user.pk, state=0))

    if settings.ALLOWED_HOSTS:
        host = f'http://{settings.ALLOWED_HOSTS[0]}'
    else:
        host = 'http://localhost:8000'

    context = {'user': user, 'host': host, 'count': count}
    subject = render_to_string('email_reports/report_letter_subject.txt', context)
    body = render_to_string('email_reports/report_letter_body.txt', context)

    user.email_user(subject, body)
