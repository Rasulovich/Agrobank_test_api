from rest_framework.serializers import ModelSerializer
from bank.models import Account, Category, Ladger


class AccountSerializer(ModelSerializer):

    class Meta:
        model = Account
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class LadgerSerializer(ModelSerializer):
    class Meta:
        model = Ladger
        fields = "__all__"