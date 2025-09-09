from django.db import models
from django.db.models import Sum

class Budget(models.Model):
    name = models.CharField(max_length=100, default="My Budget")
    initial_amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_spent(self):
        return self.expenses.aggregate(total=Sum('amount'))['total'] or 0

    def remaining(self):
        return self.initial_amount - self.total_spent()

    def __str__(self):
        return f"{self.name} ({self.initial_amount})"

class Expense(models.Model):
    budget = models.ForeignKey(Budget, related_name='expenses', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.amount}"

