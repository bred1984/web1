class test:
    ggg=4
    def __init__(self, ggg):
        self.ggg=ggg
        print('конструктор')
    def foo(self,f):
        f()
        #return self.foo1
    @staticmethod
    def foo1():
        # print(self.ggg)
        print('dcsdc')
        return
    def foo3(self):
        test.ggg=5
        print(test.ggg)

    @classmethod
    def foo4(cls):
        # cls.ggg
        print(cls.ggg)

t=test(123)
# t.foo1()
# t.foo4()
t.foo(test.foo1)
# t.foo3()
# test.foo4()
# print(t.foo())
# t.foo()()