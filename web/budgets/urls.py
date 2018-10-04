from django.urls import path
from .views import BudgetView, TransactionView, BudgetCreate, TransactionCreate

urlpatterns = [
    path('', BudgetView.as_view(), name='budget_view'),
    path('transaction/<int:id>', TransactionView.as_view(), name='transaction_view'),
    path('new', BudgetCreate.as_view(), name='budget_new'),
    path('transaction/new', TransactionCreate.as_view(), name='transaction_new'),
]
