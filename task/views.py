# Create your views here.
from django.views.generic import TemplateView, ListView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from task.models import TaskItem
from task.serializers import TaskSerializer


class Index(TemplateView):
    template_name = "base.html"


class TaskListView(ListView):
    template_name = "task/task_list.html"
    queryset = TaskItem.objects.all()


class TaskViewSet(ModelViewSet):
    """
    retrieve:
    HELLO RETRIEVE.

    list:
    HELLO LIST

    create:
    HELLO CREATE
    """

    queryset = TaskItem.objects.all()
    serializer_class = TaskSerializer

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_serializer(self, *args, **kwargs):
        if self.request and isinstance(self.request.data, list):
            kwargs["many"] = True
            print("I'm a LIST")
        else:
            print("I'm a DICT")

        return super(TaskViewSet, self).get_serializer(*args, **kwargs)
