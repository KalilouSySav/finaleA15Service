from django.db import models


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    code_projet = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    class Meta:
        app_label = 'finaleA15Service'
