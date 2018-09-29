from django.db import models

class ResultInfo(models.Model):
    student_name = models.CharField(max_length=30)
    roll = models.IntegerField()
    board_cr = (('d','Dhaka'),('j','Jessor'),('c','Comilla'))
    bord = models.CharField(max_length=13,choices= board_cr)
    school = models.CharField(max_length=40)
    gpa = models.CharField(max_length=5)


    def __str__(self):
        return self.student_name

