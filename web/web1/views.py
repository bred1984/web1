from http.client import responses

from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# from web1 import form
# import form
from web1.form import UserForm


def index(request:HttpRequest):
    # return HttpResponse("Hello METANIT.COM")
    # print(request.COOKIES)
    # # print(request.META)
    # # for  m in request.META:
    # #     print(f'Ключ: {m} ----- Значение: {request.META[m]}',)
    # # print(dict(request))
    # responses=HttpResponse('<p> Привет Мир </p>')
    # i = int(request.COOKIES['1'])
    # print(i)
    # i+=1
    # responses.set_cookie('1',str(i))
    # # HttpResponse.set_cookie
    # # return HttpResponse('<p> Привет Мир </p>')
    # return responses
    return render(request, "test1.html")

def foo(request:HttpRequest,name='Будеш хуй',age=20):
    print(request.get_full_path())
    print(request.get_host())
    print(request.get_port())
    # print(user)
    return HttpResponse(f'Имя {name}: возраст {age}')

def AddUserDB(request:HttpRequest):


    if request.method=='POST':
        name=request.POST.get('name')

        age = request.POST.get('age')
        form=UserForm(initial={'name': name,'age': age})
        print(form.name2)

        print(name,age)
        # form.
        return render(request, 'adduser.html', {'form': form})
    else:
        form = UserForm()
        return render(request,'adduser.html', {'form':form})
