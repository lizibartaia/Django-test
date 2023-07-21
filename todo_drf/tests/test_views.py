from django.test import TestCase,Client
from django.urls import reverse
from api.models import Task
from api.serializers import TaskSerializer


class TestViews(TestCase):
    
    def test_taskList_GET(self):
        client = Client()
        response =  client.get(reverse('task-list'))
        self.assertEquals(response.status_code,200)
    
    def test_taskDetail_GET(self):
        task = Task.objects.create(title='Sample Task', completed=True)
        client = Client()
        response =  client.get(reverse('task-detail', args=[task.pk]))
        self.assertEquals(response.status_code,200)
    
    
    def test_taskCreate_valid_data(self):
        client = Client()
         
        valid_data = {
            'title': 'Sample Task',
            'completed': True,
             
        }
        response = client.post(reverse('task-create'), data=valid_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(response.data, valid_data)

    def test_taskCreate_invalid_data(self):
        invalid_data = {
            'completed': False,
        }
        response = self.client.post(reverse('task-create'), data=invalid_data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Task.objects.count(), 0)

    def test_taskUpdate_valid_data(self):
        client = Client()
        valid_data = {
            'title': 'Updated Task Title',
            'completed': True,
             
        }

        task=Task.objects.create(title='Sample Task', completed=True)
        response =  client.put(reverse('task-update'), data=valid_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, valid_data['title'])
        self.assertEqual(self.task.completed, valid_data['completed'])
        serializer = TaskSerializer(self.task)
        self.assertEqual(response.data, serializer.data)

    def test_taskDelete_valid_task(self):
        client = Client()
        response = client.delete(reverse('task-delete'))
        self.assertIn(response.status_code, [200, 204])         
        with self.assertRaises(Task.DoesNotExist):
            self.task.refresh_from_db()

        self.assertEqual(response.data, "item successfully deleted!")