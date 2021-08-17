from django.db import models


class employees(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    # for string representation of class employee database
    emp_id = models.IntegerField()

    def __str__(self):
        return self.first_name
