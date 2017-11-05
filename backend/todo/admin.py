from django.contrib import admin

from .models import Task, GroupTask, Tag

class TaskAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Task._meta.fields]

    class Meta:
        model = Task

admin.site.register(Task, TaskAdmin)

class GroupTaskAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GroupTask._meta.fields]

    class Meta:
        model = GroupTask

admin.site.register(GroupTask, GroupTaskAdmin)

class TagTaskAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tag._meta.fields]

    class Meta:
        model = Tag

admin.site.register(Tag, TagTaskAdmin)