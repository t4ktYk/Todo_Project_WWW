from django.contrib import admin

from .models import TaskList, Task, Tag, Priority, Comment, SortingType


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['description', 'completed', 'task_list', 'color_filter', 'date_added']

@admin.register(SortingType)
class SortingTypeAdmin(admin.ModelAdmin):
    list_display = ['task_list', 'sort_by']


@admin.register(Tag)
class TaskTagAdmin(admin.ModelAdmin):
    pass

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


