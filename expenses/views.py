from django.shortcuts import render, redirect, get_object_or_404
from .models import Budget, Expense
from django.db.models import Sum

def set_budget(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        initial_amount = request.POST.get('initial_amount')
        budget = Budget.objects.create(name=name, initial_amount=initial_amount)
        return redirect('budget_detail', budget_id=budget.id)
    return render(request, 'set_budget.html')

def budget_detail(request, budget_id):
    budget = get_object_or_404(Budget, id=budget_id)
    if request.method == 'POST':
        desc = request.POST.get('description')
        amount = request.POST.get('amount')
        Expense.objects.create(budget=budget, description=desc, amount=amount)
        return redirect('budget_detail', budget_id=budget.id)
    total_spent = budget.total_spent()
    remaining = budget.remaining()
    return render(request, 'budget_detail.html', {
        'budget': budget,
        'expenses': budget.expenses.all(),
        'total_spent': total_spent,
        'remaining': remaining,
    })
