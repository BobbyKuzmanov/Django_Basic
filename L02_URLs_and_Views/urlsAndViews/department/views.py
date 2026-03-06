from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from urlsAndViews.department.models import Department


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, world. You're at the urlsAndViews index.</h1>")


def view_with_name(request, variable): #  Variable should be named same as URL path
    # return HttpResponse(f"<h1>Variable: {variable}</h1>")
   return render(request, 'department/name_template.html', {'variable': variable})

def view_with_int_pk(request, pk): #  pk should be primary key of your model
    # return HttpResponse(f"<h1>Primary Key: {pk}</h1>")
    return JsonResponse({"pk": pk})
def view_with_slug(request, pk, slug): #  slug should be slug of your model
    department = Department.objects.get(pk=pk, slug=slug)

    return HttpResponse(f"<h1>Department from slug: {department}</h1>")

def show_archive(request, archive_year):
    return HttpResponse(f"<h1>The year is: {archive_year}</h1>")
