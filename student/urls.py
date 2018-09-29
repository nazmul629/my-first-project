from django.urls import path
from.views import *


urlpatterns = [
     path('add/',add_studen, name = "add_students_urls"),
     path('list/',all_students, name = "student_list_urls"),
     path('delete_student/<int:id>',delete_std, name ="delete-student-urls"),
     
]