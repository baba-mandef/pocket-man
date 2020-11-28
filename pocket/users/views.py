from django.shortcuts import (render, redirect)
from pocket.users.forms import Register


def signup(request):
    if request.method == 'POST':
        form = Register(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home.html')
    else:
        form = Register
    context = {'form': form,}
    return render(request, 'registration.html', context)
