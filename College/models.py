from django.db import models


class College(models.Model):
    c_id = models.IntegerField(default=True)
    c_name = models.CharField(max_length=250)
    code = models.IntegerField(default=True)

    def __str__(self):
        return self.c_name
