from django import forms


class UserForm(forms.Form):
    name2='123'
    # def __init__(self,name1:str,age1):
    #     self.name1=name1
    #     self.age1=age1
    name = forms.CharField(initial=name2)
    age = forms.IntegerField()