from django.shortcuts import render, redirect

from new_app.forms import TodoForm
from new_app.models import Todo


def todo1(request):
    return render(request,"todo.html")
def index(request):
    return render(request,"index.html")
def index1(request):
    return render(request,"index1.html")

#create

def add(request):
    data=TodoForm()

    if request.method =='POST':
        data = TodoForm(request.POST)
        if data.is_valid:
            data.save()
            return redirect("getdata")
    return render(request,"view.html",{"data":data})

#view

def getdata(request):
    data=Todo.objects.all()
    print(data)
    return render(request,"getdata.html",{"data":data})

def update(request,Todo_id):
    todo = Todo.objects.get(id=Todo_id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('getdata')

    return render(request,'update.html',{'form':form})


def delete(request,Todo_id):
 wm=Todo.objects.get(id=Todo_id)
 wm.delete()
 return redirect("getdata")

