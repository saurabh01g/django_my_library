from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Prints Hello message'

    def handle(self, *args, **options):
        self.stdout.write(f'Hello, Programmer. This is my_Library.')