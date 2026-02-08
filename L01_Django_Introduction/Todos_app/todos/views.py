from django.http import HttpResponse
from django.shortcuts import render

from djangoProject.todos.models import Tasks


# Create your views here.
def index(request):
    tasks = Tasks.objects.all() # Fetch all tasks from the database

    context = {
        'tasks': tasks, # Pass the tasks to the template
    }


    return render(request, 'tasks/index.html', context) # MIME type: text/html




