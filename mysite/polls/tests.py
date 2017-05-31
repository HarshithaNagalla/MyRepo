from django.test import TestCase
from models import Person
from django.test.client import RequestFactory

class PollsViewsTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_index(self):
        person_1 = Person.objects.create(
            first_name = 'Harshitha',
            last_name = 'Nagalla'
        )

        #resp = self.client.get('/polls/get_name')
        resp = self.factory.get('/polls/get_name/')
        #self.assertEqual(resp.status_code, 404)
        print resp

        self.assertFalse('latest_poll_list' in resp.context)

        # self.assertEqual([poll.pk for poll in resp.context['latest_poll_list']], [1])