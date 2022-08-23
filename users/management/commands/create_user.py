from users.models import User
import factory
from factory.django import DjangoModelFactory
from django.db import transaction
from django.core.management.base import BaseCommand
from random import randint

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')


class Command(BaseCommand):
    help = 'Create user django & users to test'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write('Deleting old data...')
        User.objects.all().delete()
        count = options['count']
        number = randint(1, 100)
        user = User.objects.create_user(
            username=f'test{number}',
            email=f'django-test{number}@gb.local',
            first_name='Тест',
            last_name='Пользователей',
            password='userstesting'
        )

        self.stdout.write('Creating new users...')
        people = []
        for _ in range(count):
            person = UserFactory()
            people.append(person)
            print(f'User {user.username} created.')
        print('Done!')
