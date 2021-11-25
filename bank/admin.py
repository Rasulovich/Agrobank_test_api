from django.contrib import admin
from .models import Account, Category, Ladger

admin.site.register([
    Account,
    Category,
    Ladger
])
