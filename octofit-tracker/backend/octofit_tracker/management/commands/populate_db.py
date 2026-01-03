from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Skipping deletion of old data. Please drop collections using mongosh before running this command if you want a clean state.'))

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel Super Heroes')
        dc = Team.objects.create(name='DC', description='DC Super Heroes')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(user=users[0], type='Run', duration=30, date='2023-01-01')
        Activity.objects.create(user=users[1], type='Swim', duration=45, date='2023-01-02')
        Activity.objects.create(user=users[2], type='Bike', duration=60, date='2023-01-03')
        Activity.objects.create(user=users[3], type='Run', duration=25, date='2023-01-01')
        Activity.objects.create(user=users[4], type='Swim', duration=50, date='2023-01-02')
        Activity.objects.create(user=users[5], type='Bike', duration=70, date='2023-01-03')

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        w1 = Workout.objects.create(name='Pushups', description='Upper body strength')
        w2 = Workout.objects.create(name='Situps', description='Core strength')
        w1.suggested_for.set([users[0], users[3]])
        w2.suggested_for.set([users[1], users[4]])

        self.stdout.write(self.style.SUCCESS('Creating leaderboards...'))
        Leaderboard.objects.create(team=marvel, score=135)
        Leaderboard.objects.create(team=dc, score=145)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
