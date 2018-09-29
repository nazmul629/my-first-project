from django.db import models

class StudentInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender_ls = (('m','Male'),('f','Female'))
    gender = models.CharField(max_length = 10, choices = gender_ls)
    fathers_name =models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile_nember = models.IntegerField()


    def __str__(self):
        return self.name