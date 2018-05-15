import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Expert
from ..serializers import ExpertSerializer
from .. import views

client = Client()


class ExpertListTest(TestCase):
    def setUp(self):

        expert_hans = Expert.objects.create(
            first_name="Hans",
            last_name="Nestor",
            email_address="wnestor@netsorw.com",
            short_description="Teacher - English",
            full_description="English teacher",
            university="University of Cologne",
            major="English",
            popularity=3,
            path_to_picture="pic3",
            hourly_rate=50,
            deleted=1,
            total_hours_taught=100
            )

        expert_hans.save()

        expert_jeff = Expert.objects.create(
            first_name="Jeff",
            last_name="Dean",
            email_address="jdean@netsorw.com",
            short_description="Teacher - Algorithms",
            full_description="Algorithms teacher",
            university="University of Califonia",
            major="Algorithms",
            popularity=5,
            path_to_picture="pic5",
            hourly_rate=50,
            deleted=1,
            total_hours_taught=100
            )
        expert_jeff.save()

    def test_get_all_experts(self):

        response = client.get(reverse('get'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ExpertDetailtest(TestCase):
    def setUp(self):

        expert_hans = Expert.objects.create(
            first_name="Hans",
            last_name="Nestor",
            email_address="wnestor@netsorw.com",
            short_description="Teacher - English",
            full_description="English teacher",
            university="University of Cologne",
            major="English",
            popularity=3,
            path_to_picture="pic3",
            hourly_rate=50,
            deleted=1,
            total_hours_taught=100
            )

        expert_hans.save()

        expert_jeff = Expert.objects.create(
            first_name="Jeff",
            last_name="Dean",
            email_address="jdean@netsorw.com",
            short_description="Teacher - Algorithms",
            full_description="Algorithms teacher",
            university="University of Califonia",
            major="Algorithms",
            popularity=5,
            path_to_picture="pic5",
            hourly_rate=50,
            deleted=1,
            total_hours_taught=100
            )
        expert_jeff.save()

    def test_retrieve_single_expert(self):
        response = client.get(reverse('detail', kwargs={"pk": 2}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

