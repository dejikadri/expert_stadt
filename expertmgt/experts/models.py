from django.db import models


class Expert(models.Model):
    """
    This Model allows contains the definition for Experts

    """
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email_address = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    full_description = models.TextField()
    university = models.CharField(max_length=250)
    major = models.CharField(max_length=250)
    popularity = models.IntegerField()
    path_to_picture = models.CharField(max_length=150)
    hourly_rate = models.FloatField()
    total_hours_taught = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Unicode representation of Experts.
        """
        return "{} {} - ({})".format(self.first_name, self.last_name, self.short_description) 
