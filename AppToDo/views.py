from django.shortcuts import render, redirect
from AppToDo.models import TodoItem
from django.http import HttpResponseRedirect
#from django.contrib.admin import
# Create your views here.

def base(request):
    return render(request,'base.html')

def todoView(request):
    # to display TodoItem
    all_todo_item = TodoItem.objects.all()
    dict = {
           'all_item':all_todo_item
           }
    return render(request,'AppToDo/todo.html',context=dict)

def addTodo(request):
    # create new todo all_item
    # save
    # redirect to original
    c = request.POST['content']
    new_item = TodoItem(content=c)
    new_item.save()
    return redirect('/AppToDo/')


def deleteTodo(request,todo_id):
    # delete
    # save
    # redirect to original
    item = TodoItem.objects.get(id=todo_id)
    item.delete()
    return redirect('/AppToDo/')
