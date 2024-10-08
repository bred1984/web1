from django import forms


class UserForm(forms.Form):
    name2='123'
    # def __init__(self,name1:str,age1):
    #     self.name1=name1
    #     self.age1=age1
    name = forms.CharField(initial='Введите имя')
    age = forms.IntegerField(initial='Введите возраст')
    pasport = forms.CharField(initial='Введите паспорт')