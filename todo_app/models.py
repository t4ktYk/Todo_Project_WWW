from django.contrib.auth.models import User
from django.db import models

class TaskList(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Task(models.Model):
    color_choices = (
        ('default-filter-color', 'default-filter-color'),
        ('color-filter-red', 'color-filter-red'),
        ('color-filter-orange', 'color-filter-orange'),
        ('color-filter-green', 'color-filter-green'),
        ('color-filter-cyan', 'color-filter-cyan'),
        ('color-filter-blue', 'color-filter-blue'),
        ('color-filter-purple', 'color-filter-purple'),
    )

    description = models.TextField()
    completed = models.BooleanField(default=False)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    color_filter = models.CharField(max_length=20, choices=color_choices, default='default-filter-color')

    def __str__(self):
        return self.description

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Priority(models.Model):
    LEVEL_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)

    def __str__(self):
        return self.level

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.task.description}"