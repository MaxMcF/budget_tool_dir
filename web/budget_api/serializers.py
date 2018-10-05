from django.contrib.auth.models import User
from rest_framework import serializers
from budgets.models import Budget, Transaction


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = super().create({
            'username': validated_data['username'],
            'email': validated_data['email'],
        })

        user.set_password(validated_data['password'])
        user.save()
        return user

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'description', 'amount')

class BudgetSerializer(serializers.ModelSerializer):
    transaction = TransactionSerializer(many=True)
    class Meta:
        model = Budget
        fields = ('id', 'name', 'total_budget', 'remaining_budget', 'transaction', 'date_uploaded', 'date_modified')
