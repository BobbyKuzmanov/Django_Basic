from django.contrib import admin

from djangoProject.todos import models


# Register your models here.
@admin.register(models.Tasks)
class TaskAdmin(admin.ModelAdmin):
    pass