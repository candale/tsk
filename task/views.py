# Create your views here.
from django.views.generic import TemplateView, ListView

from task.models import TaskItem


class Index(TemplateView):
    template_name = "base.html"


class TaskListView(ListView):
    template_name = "task/task_list.html"
    queryset = TaskItem.objects.all()
