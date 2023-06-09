from django.core.management import BaseCommand

from ...utils import send_user_report


class Command(BaseCommand):
    help = "Send Today's Report to Admins"

    def handle(self, *args, **options):
        from accounts.models import User
        for user in User.objects.filter(results__state=0).distinct():
            send_user_report(user)
