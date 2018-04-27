from django.db import models


class Expert(models.Model):
    """
    This Model allows contains the definition for Experts

    """
   full_name =  models.CharField(max_length=150)
   email_address = models.CharField(max_length=100)
   short_description =  models.CharField(max_length=200)
   full_description =  models.TextField()
   popularity =  models.IntegerField()
   path_to_picture =  models.CharField(max_length=150)
   hourly_rate =  models.FloatField()
   total_hours_taught =  models.IntegerField()


    def __str__(self):
        """
        Unicode representation of Experts.
        """
        return self.
