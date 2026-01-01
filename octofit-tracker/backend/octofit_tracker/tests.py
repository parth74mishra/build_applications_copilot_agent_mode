from django.test import TestCase
from rest_framework.test import APIClient
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team)
        self.workout = Workout.objects.create(name='Web Swing', description='Swinging workout')
        self.activity = Activity.objects.create(user=self.user, type='Cardio', duration=30, date='2025-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, score=100, week=1)

    def test_user_str(self):
        self.assertEqual(str(self.user), 'Spider-Man')
    def test_team_str(self):
        self.assertEqual(str(self.team), 'Marvel')
    def test_activity_str(self):
        self.assertIn('Spider-Man', str(self.activity))
    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Web Swing')
    def test_leaderboard_str(self):
        self.assertIn('Marvel', str(self.leaderboard))

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='DC', description='DC Team')
        self.user = User.objects.create(name='Batman', email='batman@dc.com', team=self.team)

    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.data)
    def test_users_endpoint(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
