from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import  TodoForm
from .models import ToDo


def index(request):
    item_list = ToDo.objects.order_by('-date')
    if request.method  == 'POST':
        form = ToDo.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()
    page = {
        'forms': form,
        'list':item_list,
        'title':'TODO LIST',
    }
    return render(request,'todo/index.html',page)


def remove(request, item_id):
    item = ToDo.objects.get(id=item_id)
    item.delete()
    messages.info(request, 'Item deleted')
    return redirect('todo')



