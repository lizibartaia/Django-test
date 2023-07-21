from django.test import SimpleTestCase
from django.urls import reverse,resolve
from api.views import taskList,taskDetail,taskCreate,taskUpdate,taskDelete



class TestUrls(SimpleTestCase):
    def test_tasklist_url_resolves(self):
        url = reverse('task-list')
        print(resolve(url))
        self.assertEquals(resolve(url).func,taskList)

    def test_taskCreate_url_resolves(self):
        url = reverse('task-create')
        print(resolve(url))
        self.assertEquals(resolve(url).func,taskCreate)
    
    def test_taskDetail_url_resolves(self):
        url = reverse('task-detail',args=['pk'])
        print(resolve(url))
        self.assertEquals(resolve(url).func,taskDetail)
    
    def test_taskUpdate_url_resolves(self):
        url = reverse('task-update',args=['pk'])
        print(resolve(url))
        self.assertEquals(resolve(url).func,taskUpdate)
    
    def test_taskDelete_url_resolves(self):
        url = reverse('task-delete',args=['pk'])
        print(resolve(url))
        self.assertEquals(resolve(url).func,taskDelete)
    

        
 
     
