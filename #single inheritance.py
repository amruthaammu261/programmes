#single inheritance

class parent:#class difinition
    def function1(self):
        print("It is a function1")
    def function2(self):
        print("It is a function12")
class child(parent):#class definition
    def function3(self):
        print("It is a function3")
    def function4(self):
        print("It is a function4")
#main program
c1 = child()#object Declaration
c1.function1()#function call
c1.function2()#function call
c1.function3()#function call
c1.function4()#function call


