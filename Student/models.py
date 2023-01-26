from django.db import models


class Student(models.Model):
    s_id = models.IntegerField(default=20)
    s_name = models.CharField(max_length=250)
    CATEGORY_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    s_gender = models.CharField(max_length=200, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.s_name + ' - ' + self.s_gender
