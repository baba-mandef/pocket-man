from django.shortcuts import render, redirect
from datetime import datetime, date
from statistics import mean
from pocket.manager.models import Activity
from pocket.manager.forms import ActivityForm


def home(request):
    if not request.user.is_authenticated:
        context = {}
    else:
        today = datetime.today()
        month = today.month
        month = int(month)
        year = int(today.year)
        latest_incomes = Activity.objects.filter(owner=request.user, is_gain=True, date__month=month, date__year=year)[:10]
        latest_expenses = Activity.objects.filter(owner=request.user, is_spent=True, date__month=month, date__year=year)[:10]
        current_month_incomes = Activity.objects.filter(owner=request.user, is_gain=True, date__month=month, date__year=year)
        current_month_expenses = Activity.objects.filter(owner=request.user, is_spent=True, date__month=month, date__year=year)
        incomes_amount = []
        expenses_amount = []
        for amount in current_month_expenses:
            expenses_amount.append(int(amount.amount))
        if len(expenses_amount) > 1:
            spent_avg = mean(expenses_amount)
        else:
            spent_avg = "Add more expenses"
        for amount in current_month_incomes:
            incomes_amount.append(int(amount.amount))
        if len(incomes_amount) > 1:
            gain_avg = mean(incomes_amount)
        else:
            gain_avg = "Add more incomes"

        context = {'latest_incomes': latest_incomes,
                   'latest_expenses': latest_expenses,
                   'gain_avg': gain_avg,
                   'spent_avg': spent_avg,
                   'month': month}
    return render(request, 'home.html', context)


def add_expense(request):
    if request.method == 'POST':
        form = ActivityForm(data=request.POST)
        if form.is_valid():
            new_expense = form.save(commit=False)
            new_expense.owner = request.user
            new_expense.is_spent = True
            new_expense.is_gain = False
            new_expense.save()
        return redirect('/')
    else:
        form = ActivityForm()
    context = {'form': form}
    return render(request, 'expense.html', context)


def del_activity(request, id):
    income = Activity.objects.get(id=id)
    income.delete()
    return redirect('/')


def add_income(request):
    if request.method == 'POST':
        form = ActivityForm(data=request.POST)
        if form.is_valid():
            new_income = form.save(commit=False)
            new_income.owner = request.user
            new_income.is_spent = False
            new_income.is_gain = True
            new_income.save()
        return redirect('/')
    else:
        form = ActivityForm()
    context = {'form': form}
    return render(request, 'income.html', context)


def monthly_incomes(request, month):
    today = datetime.today()
    y = today.year
    m = date(y, month, 1).strftime('%B')
    monthly = Activity.objects.filter(owner=request.user, is_gain=True, date__month=month, date__year=y)
    monthly_lst = []
    for lst in monthly:
        monthly_lst.append(int(lst.amount))
    if len(monthly_lst) > 1:
        monthly_avg = mean(monthly_lst)
    else:
        monthly_avg = "Add more incomes"
    total = sum(monthly_lst)
    context = {'monthly': monthly, 'monthly_avg': monthly_avg, 'total': total, 'm': m, }
    return render(request, 'ihistory.html', context)


def monthly_expense(request, month):
    monthly_amount = []
    today = datetime.today()
    y = today.year
    m = date(y, month, 1).strftime('%B')
    monthly_query = Activity.objects.filter(owner=request.user, is_spent=True, date__month=month, date__year=y)
    for amount in monthly_query:
        monthly_amount.append(int(amount.amount))
    if len(monthly_amount) > 1:
        monthly_avg = mean(monthly_amount)
    else:
        monthly_avg = "Add more expenses"
    total = sum(monthly_amount)
    context = {'monthly': monthly_query, 'monthly_avg': monthly_avg, 'total': total, 'm': m, }
    return render(request, 'ehistory.html', context)
