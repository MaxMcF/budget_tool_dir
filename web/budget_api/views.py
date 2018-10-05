from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import UserSerializer, BudgetSerializer, TransactionSerializer
from .serializers import User, Budget, Transaction


class RegisterApiView(generics.CreateAPIView):
    permission_classes = ''
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer

class UserApiView(generics.RetrieveAPIView):
    permission_classes = ''
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])

class BudgetApiView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(user__username=self.request.user.username)

class TransactionApiView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(budget__user__username=self.request.user.username)
