from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from .serializers import UserSerializer, User


class RegisterApiView(generics.CreateAPIView):
    permission_classes = ''
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer


class UserApiView(generics.RetrieveAPIView):
    permission_classes = ''
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])

class BudgetApiView(generics.RetrieveAPIView):
    permission_classes = ''
    serialzer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(user__username=self.request.user.username)
