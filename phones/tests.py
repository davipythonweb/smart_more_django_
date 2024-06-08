from django.test import TestCase
from django.urls import reverse

class PhonesURLsTest(TestCase):  
    def test_pytest_is_ok(self):
        assert 1 == 1, 'um rh igual a um.'
        
    def test_phones_list_url_is_correct(self):
        url = reverse('namespace:list')
        self.assertEqual(url, '/')
        
    def test_phones_new_url_is_correct(self):
        url = reverse('namespace:new')
        self.assertEqual(url, '/new_phone/')
        
    def test_phones_detail_url_is_correct(self):
        url = reverse('namespace:detail', kwargs={'pk': 1})
        self.assertEqual(url, '/phone/1')
        
    def test_phones_update_url_is_correct(self):
        url = reverse('namespace:update', kwargs={'pk':1})
        self.assertEqual(url, '/phone/1/update')
        
    def test_phones_delete_url_is_correct(self):
        url = reverse('namespace:delete', kwargs={'pk':1})
        self.assertEqual(url, '/phone/1/delete')
    