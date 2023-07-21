from django.test import TestCase
from api.models import Task   

class TestTaskModelTestCase(TestCase):
    def test_model_save_and_retrieve(self):
        task = Task.objects.create(title='Sample Task', completed=False)
        retrieved_task = Task.objects.get(id=task.id)
        self.assertEqual(task.title, retrieved_task.title)
        self.assertEqual(task.completed, retrieved_task.completed)

    def test_model_update(self):
        task = Task.objects.create(title='Sample Task', completed=False) 
        updated_title = 'Updated Task Title'
        updated_completed = True
        task.title = updated_title
        task.completed = updated_completed
        task.save()
        retrieved_task = Task.objects.get(id=task.id)
        self.assertEqual(task.title, retrieved_task.title)
        self.assertEqual(task.completed, retrieved_task.completed)

    def test_model_delete(self):
        task = Task.objects.create(title='Sample Task', completed=False)
        task.delete()
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=task.id)