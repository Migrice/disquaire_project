from django.test import TestCase
from django.urls import reverse
from .models import Contact, Booking,Album, Artist
#unitest est le module de test par defaut dans django

# Create your tests here.
# Index page
class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response= self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    # test that index page returns a 200

# Detail Page
class DetailPageTestCase(TestCase):
    def test_detail_page_return_200(self):
        impossible=Album.objects.create(title="Transmission impossible")
        album_id=Album.objects.get(title="Transmission impossible").id
        response=self.client.get(reverse('store:detail',args=(album_id,)))
        self.assertEqual(response.status_code, 200)

    # test that detail page returns a 200 if the item exists
    # test that detail page returns a 404 if the item does not exist

# Booking Page
    # test that a new booking is made
    # test that a booking belongs to a contact
    # test that a booking belongs to an album
    # test that an album is not available after a booking is made