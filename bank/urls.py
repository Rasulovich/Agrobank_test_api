from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bank.views import AccountViewSet, CategoryViewSet, LadgerViewSet

router = DefaultRouter()
router.register('account', AccountViewSet)
router.register('category', CategoryViewSet)
router.register('ladger', LadgerViewSet)


urlpatterns = [

    path('', include(router.urls))

]