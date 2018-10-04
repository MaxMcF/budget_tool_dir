from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
from django.db import models

# Create your models here.
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budget')
    name = models.CharField(max_length=180, default='Untitled')

    total_budget = models.FloatField(blank=True, null=True)
    remaining_budget = models.FloatField(blank=True, null=True)

    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __repr__(self):
        return '<Budget: {}>'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)

class Transaction(models.Model):

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='transaction')
    description = models.CharField(max_length=180, default='No Description')
    amount = models.FloatField(blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    STATES = (
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAWL', 'Withdrawl'),
    )
    action_type = models.CharField(
        max_length=16,
        choices=STATES,
    )

    def __repr__(self):
        return '<Transaction: {}>'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)
