from datetime import datetime

from django.db import models

# Create your models here.
from django.db.models import CASCADE
from django.db.models.signals import pre_save

from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage, SELF


class TaskItem(models.Model):
    title = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey("auth.User", models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


def send_task_notification(sender, instance, *args, **kwargs):
    if instance.id is None:
        publisher = RedisPublisher(facility='notify', users=['candale'])
        publisher.publish_message(
            RedisMessage(
                '{} - {}'.format(
                    instance.title, datetime.today().isoformat()
                )
            )
        )


pre_save.connect(send_task_notification, TaskItem)
