import os

from django.core.management.base import BaseCommand, CommandError
from ._private import CsvImporter


class Command(BaseCommand):
    help = "import the channels categories from a CSV"

    def add_arguments(self, parser):
        parser.add_argument('channel')
        parser.add_argument('file')

    def handle(self, *args, **options):
        channel = options['channel'].lower()
        file = options['file']

        if not channel or not file:
            raise Exception("CommandError: the following arguments are required: channel, file")

        if not os.path.isfile(file):
            raise Exception("File does not exists")
        else:

            csv = CsvImporter(channel, file)
            csv.process()
            self.stdout.write("ok")


