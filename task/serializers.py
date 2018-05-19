from rest_framework.serializers import ModelSerializer

from task.models import TaskItem


class TaskSerializer(ModelSerializer):
    class Meta:
        model = TaskItem
        fields = "__all__"