from django.test import TestCase
from .. import models
from ..models import Expert


class ExpertModelTest(TestCase):
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

    def test_retrieve_rexpert(self):
            expert_hans2 = Expert.objects.get(first_name="Hans")
            # print(expert_hans2.first_name, "xxxxxxxxxxxx")
            self.assertEqual("Hans", expert_hans2.first_name)

    def test_create_records(self):
        expert_hans2 = Expert.objects.all()
        print("OOOOOOOOOOOO", expert_hans2.count())