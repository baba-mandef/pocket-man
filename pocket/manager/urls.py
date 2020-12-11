from django.urls import path
from pocket.manager.views import (home, add_expense, add_income, del_activity, monthly_incomes, monthly_expense)

urlpatterns = [

    path('', home, name='home'),
    path('expenses/add', add_expense, name='expense'),
    path('incomes/add', add_income, name='income'),
    path('activity/delete/<int:id>', del_activity, name='delete'),
    path('incomes/history/<int:month>', monthly_incomes, name='incomes_history'),
    path('expenses/history/<int:month>', monthly_expense, name='expenses_history'),

]
