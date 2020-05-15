from django.core.management.base import BaseCommand
from users_app.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        for item in users:

            print(item.email)
            print(item.companies.all())
        print('---------------')
        user = User.objects.get(email='brandy73@bass.com')
        print(user)
        print('---------------')
        companies = user.companies.all()
        print(len(companies))
        for item in companies:
            print(item.name)
        print('---------------')
