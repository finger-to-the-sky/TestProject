from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from users.models import User, AccountBalance


class UserModelSerializers(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

class BalanceModelSerializer(ModelSerializer):
    class Meta:
        model = AccountBalance
        fields = ('user_id', 'balance')
