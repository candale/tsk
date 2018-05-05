from django.contrib import admin

# Register your models here.
from task.models import TaskItem


class TaskModelAdmin(admin.ModelAdmin):
    list_display = ["title", "due_date", "done", "created_at", "owner"]
    list_filter = ["done", "owner"]
    search_fields = ["title", "owner__email"]


admin.site.register(TaskItem, TaskModelAdmin)