from rest_framework.viewsets import ModelViewSet

from users.models import User, AccountBalance
from users.serializers import UserModelSerializers, BalanceModelSerializer

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializers

class BalanceModelViewSet(ModelViewSet):
    queryset = AccountBalance.objects.all()
    serializer_class = BalanceModelSerializer