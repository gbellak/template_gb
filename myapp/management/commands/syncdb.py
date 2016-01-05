from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Workaround'
    def handle(self, *args, **options):
        pass