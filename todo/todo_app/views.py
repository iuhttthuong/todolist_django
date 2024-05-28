from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Task

from .forms import TaskForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()


    tasks = Task.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'tasks': tasks,
        'form': form,
    }
    return HttpResponse(template.render(request=request, context=context))

def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect(reverse('index'))

def testing(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testing')
    else:
        form = TaskForm()

    tasks = Task.objects.all().values()
    context = {
        'tasks': tasks,
        'form': form,
    }

    return render(request, 'testing.html', {'form': form, 'tasks': tasks})

# def testing(request):
#     if request.method == 'POST':
    
#         form = NameForm (request.POST) # tạo một thể hiện biểu mẫu và điền nó với dữ liệu từ yêu cầu:
    
#         if form.is_valid (): # kiểm tra xem nó có hợp lệ không
    
#             # xử lý dữ liệu trong form.cleaned_data theo yêu cầu
#             a = request.POST['your_name']
#             print(a)
#             # form.save()
#             # return redirect('testing')
#             return render (request, 'testing.html', {'form': form, 'a': a})

#     #if a GET (hoặc bất kỳ phương thức nào khác), chúng ta sẽ tạo một biểu mẫu trống
#     else: 
#         a = "none"
#         form = NameForm()
    
#     return render (request, 'testing.html', {'form': form, 'a': a})

