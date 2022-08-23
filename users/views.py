from rest_framework.viewsets import ModelViewSet

from users.models import User, Account_Balance
from users.serializers import UserModelSerializers, BalanceModelSerializer

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializers

class BalanceModelViewSet(ModelViewSet):
    queryset = Account_Balance.objects.all()
    serializer_class = BalanceModelSerializer