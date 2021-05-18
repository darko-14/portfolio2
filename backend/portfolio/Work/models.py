from django.db import models

class Work(models.Model):
    project_title = models.CharField(max_length=100)
    project_description = models.TextField(max_length=500)
    project_img = models.ImageField
    github_link = models.CharField(max_length=100, blank=True)
    app_link = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.project_title
