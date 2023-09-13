from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
        
    #Penambahan test.py
    def setUp(self):
        Item.objects.create(name="semen",amount="500",
                        description="semen terbaik yang dijual",price="45000")
        Item.objects.create(name="kayu",amount="700",
                        description="kayu merupakan hal yang penting dalam membuat rumah",price="20000")
    
    def test_items_can_created(self):
        semen = Item.objects.get(name="semen")
        kayu = Item.objects.get(name="kayu")
        self.assertEqual(semen.name, "semen")
        self.assertEqual(kayu.name, "kayu")
        self.assertEqual(semen.amount, 500)
        self.assertEqual(kayu.amount, 700)
        self.assertEqual(semen.price, 45000)
        self.assertEqual(kayu.price, 20000)
        