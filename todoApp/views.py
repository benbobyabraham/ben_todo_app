from django.shortcuts import render, redirect
from .forms import todo_form
from .models import itemTodo
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    mytodo = itemTodo.objects.order_by('done', 'id')
    form = todo_form()
    context = {'mytodo': mytodo, 'form': form}
    return render(request, 'todoApp/index.html', context)

@require_POST
def add_new_todo(request):
    form = todo_form(request.POST)

    if(form.is_valid()):
        new_todo = itemTodo(desc = request.POST['desc'])
        new_todo.save()

    return redirect('index')

def done_todo(request, todo_id):
    mytodo = itemTodo.objects.get(id = todo_id)
    mytodo.done = True
    mytodo.save()
    return redirect('index')

def undone_todo(request, todo_id):
    mytodo = itemTodo.objects.get(id = todo_id)
    mytodo.done = False
    mytodo.save()
    return redirect('index')

def delete_todo(request):
    mytodo = itemTodo.objects.filter(done__exact=True).delete()
    return redirect('index')
