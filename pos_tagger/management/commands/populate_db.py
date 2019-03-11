from django.core.management.base import BaseCommand
from pos_tagger.service import create_super_user, generate_tags


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_tags(self):
        create_super_user()
        generate_tags()

    def handle(self, *args, **options):
        self._create_tags()
