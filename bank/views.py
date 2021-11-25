from django.shortcuts import render
from .models import Category, Ladger, Account
from rest_framework.viewsets import ModelViewSet
from .serializer import AccountSerializer, CategorySerializer, LadgerSerializer


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LadgerViewSet(ModelViewSet):
    queryset = Ladger.objects.all()
    serializer_class = LadgerSerializer






