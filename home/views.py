from django.shortcuts import render 
from home.models import Tasks

# Create your views here.
def home(request):
    context = {'success': False ,'name' : 'Shivani'}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        task = Tasks(taskTitle=title, taskDesc=desc)
        task.save()
        context = {'success': True}
    return render(request, 'index.html', context)


def tasks(request):
    allTasks = Tasks.objects.all()
    # print(allTasks)
    # for item in allTasks:
    #     print(item.taskTitle)
    context = {'tasks':allTasks}
    return render(request,'tasks.html' ,context)

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        tasks = Tasks.objects.filter(taskTitle__contains = searched)
        return render(request, 'search.html', {'searched': searched, 'tasks':tasks})
    else:
       return render(request, 'search.html', {})
