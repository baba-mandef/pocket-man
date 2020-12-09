from django.shortcuts import render, redirect
from pocket.manager.forms import ActivityForm


def home(request):
    context = {}
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
