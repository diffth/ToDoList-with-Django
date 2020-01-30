from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    contentDic = {'todos':todos}
    return render(request, 'my_to_do_app/index.html', contentDic)
    # return HttpResponse("my_to_do_app first page")

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse("create Todo를 할꺼야 => " + user_input_str)
    # return HttpResponse("create Todo를 할꺼야!")
