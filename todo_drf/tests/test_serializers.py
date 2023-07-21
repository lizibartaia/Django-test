from django.test import TestCase
from api.models import Task   
from api.serializers import TaskSerializer  

class TestTaskSerializerTestCase(TestCase):
    def test_serializer_with_correct_data(self): 
        correct_data = {
            'title': 'Sample Task',
            'completed': True,
             
        }
        serializer = TaskSerializer(data=correct_data)
        self.assertTrue(serializer.is_valid()) 
        self.assertEqual(serializer.validated_data['title'], correct_data['title'])
        self.assertEqual(serializer.validated_data['completed'], correct_data['completed'])
      

    def test_serializer_with_incorrect_data(self):
        incorrect_data = {
            'completed': True,
        }
        serializer = TaskSerializer(data=incorrect_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)