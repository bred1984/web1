from http.client import responses

from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# from web1 import form
# import form
# from web1.form import UserForm

from SqlDriver import SqlDriver
from form import UserForm


def index(request:HttpRequest):
    return render(request, "test1.html")

def foo(request:HttpRequest,name='Будеш хуй',age=20):
    print(request.get_full_path())
    print(request.get_host())
    print(request.get_port())
    # print(user)
    return HttpResponse(f'Имя {name}: возраст {age}')

def InsertUserDB(request:HttpRequest):
    if request.method=='POST':
        form=UserForm(request.POST)#
        if form.is_valid():
            # form.cleaned_data['name']
            # form.cleaned_data['age']
            name=form.cleaned_data['name']
            if ' ' in   name:
                return HttpResponse(' Дич')
            form=UserForm()
            print(request.POST)
            data={}
            data['fio']=request.POST.get('name')
            data['age'] = request.POST.get('age')
            data['pasport'] = request.POST.get('pasport')
            status="Все ок"
            # sql = SqlDriver()
            # sql.connect(sql.insert_db,data)
            SqlDriver.connect(SqlDriver.insert_db,data)

            return render(request, 'adduser.html', {'form': form,'status':'Все ок'})
        else:
            return render(request, 'adduser.html', {'form': form,'status':'Не верно ввел'})

    else:
        form = UserForm()
        return render(request,'adduser.html', {'form':form})

def CreateDB(request):
    sql=SqlDriver()
    sql.connect(sql.CreateDB)
    # sql.CreateDB()
    return HttpResponse('Таблицы созданы')
