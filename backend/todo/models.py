from django.db import models


class GroupTask(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=256)
    group = models.ForeignKey(GroupTask, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32)
    task = models.ManyToManyField(Task)

    def __str__(self):
        return self.name