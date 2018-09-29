from django.urls import path
from.views import *


urlpatterns = [
    path('create/', create_result, name = "creat_result_urls"),
    path('list/', all_result, name = "resul_list_urls"),
    path('chek/',cheke_result, name= "cheke_result_urls"),
    path('school/<school_num>', school_result, name = "school_result_url"),
    path('board/<board_num>', board_result, name = "board_num_url")
]