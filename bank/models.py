from django.db import models


class Account(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    initial_balance = models.DecimalField(decimal_places=2, max_digits=20)
    created_on = models.DateField()
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class Category(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(null=True, blank=True)
    budget = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Ladger(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    payee = models.CharField(max_length=256)

    def __str__(self):
        return self.payee