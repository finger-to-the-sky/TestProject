from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from users.models import User, Account_Balance


class UserModelSerializers(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

class BalanceModelSerializer(ModelSerializer):
    class Meta:
        model = Account_Balance
        fields = ('balance',)
