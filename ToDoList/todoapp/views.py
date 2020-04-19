from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import TodoList

# Create your views here.
def todo(request):
    all_todo_items = TodoList.objects.all()
    return render(request , "todo.html" , {"all_items":all_todo_items})

def addtodo(request):
    new_item = TodoList(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect("/")   

def deletetodo(request, todo_id):
    todoitem = TodoList.objects.get(id=todo_id)
    todoitem.delete()
    return HttpResponseRedirect("/")   