import csv

from django.core.management.base import BaseCommand
from django.utils import timezone

from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Import squirrel csv'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_csv')

    def handle(self, *args, **options):
        with open(options['squirrel_csv']) as fp:
            reader = csv.DictReader(fp)
            noduplicates = list()

            for item in reader:
                if item['Unique Squirrel ID'] in noduplicates:
                    continue
                else:
                    obj = Squirrel()
                    obj.longitude = float(item['X']),
                    obj.latitude = float(item['Y']),
                    obj.unique_squirrel_id = item['Unique Squirrel ID'],
                    obj.shift = item['Shift'].lower(),
                    obj.date  = timezone.datetime.strptime(item['Date'], '%m%d%Y').date(),
                    obj.age = item['Age'],
                    obj.primary_fur_color = item['Primary Fur Color'],
                    obj.specific_location = item['Specific Location'],
                    obj.running = item['Running'] == 'TRUE',
                    obj.chasing = item['Chasing'] == 'TRUE',
                    obj.climbing = item['Climbing'] == 'TRUE',
                    obj.eating = item['Eating'] == 'TRUE',
                    obj.foraging = item['Foraging'] == 'TRUE',
                    obj.other_activities = item['Other Activities'] == 'TRUE',
                    obj.kuks = item['Kuks'] == 'TRUE',
                    obj.quaas = item['Quaas'] == 'TRUE',
                    obj.moans = item['Moans'] == 'TRUE',
                    obj.tail_flags = item['Tail flags'] == 'TRUE',
                    obj.tail_twitches = item['Tail twitches'] == 'TRUE',
                    obj.approaches = item['Approaches'] == 'TRUE',
                    obj.indifferent = item['Indifferent'] == 'TRUE',
                    obj.runs_from = item['Runs From'] == 'TRUE',
                    
                    obj.save()
                    noduplicates.append(item['Unique Squirrel ID'])
