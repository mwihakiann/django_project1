from django.test import TestCase
from .models import Task

# Create your tests here.
class TaskModelTests(TestCase):
    def test_create_task(self):
        task = Task.objects.create(title="Test Task")
        self.assertEqual(task.title, "Test Task")