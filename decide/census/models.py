from django.db import models
from django.core.exceptions import ValidationError


class Census(models.Model):
    voting_id = models.PositiveIntegerField()
    voter_id = models.PositiveIntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    region = models.CharField(max_length=100)

    # A new census is valid if the pair is not already in the database
    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if Census.objects.filter(voting_id=self.voting_id, voter_id=self.voter_id).exists():
            raise ValidationError(
                'There is already exists this pair', code='Error')
