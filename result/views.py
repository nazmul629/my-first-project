from django.shortcuts import render
from .models import *
from.forms import *
from django.contrib.auth.decorators import login_required

@login_required
def create_result(request):
    if request.method =='POST':
        form = AddResultForm(request.POST)
        if form.is_valid():
            form.save()
    form = AddResultForm()
    contxt = {'forms':form}
    return render (request,'result/add_result.html',contxt)


def all_result(request):
    result_list = ResultInfo.objects.all()
    contex = {'all_result':result_list}
    return render (request,'result/result_list.html',contex)


def cheke_result(request):
    if request.method =='POST':
        form = ChakeResultForm(request.POST)
        if form.is_valid():
            roll_no = form.cleaned_data["roll"]
            try:
                roll_obj = ResultInfo.objects.get(roll = roll_no)
                print(roll_obj)
                contxt = {'roll':roll_obj.objects.roll,
                          'name':roll_obj.objects.name,
                          'gpa': roll_obj.objects.gpa,
                          'forms':form
                          }
                return render (request,'result/chekresult.html',contxt)
            
            except:

                contxt = {'Error':"Not found result",
                            'forms':form
                            }
                return render (request,'result/chekresult.html',contxt)




    form = ChakeResultForm()
    contxt = {'forms':form}
    return render (request,'result/chekresult.html',contxt)



def school_result(request,school_num):
    all_result = ResultInfo.objects.filter(school = school_num)
    context = {'schoolresult':all_result}
    print("Quri set iare ",context)
    return render(request,'result/schoolresult.html',context)


def board_result(request,board_num):
    all_result = ResultInfo.objects.filter(bord = board_num)
    context = {'schoolresult':all_result}
    print("Quri set iare ",context)
    return render(request,'result/schoolresult.html',context)