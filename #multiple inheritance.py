#multiple inheritance

class parent1:
    def function1(self):
        print("This is a parent1 function")
class parent2:
    def function2(self):
        print("This is a parent2 function")
class child(parent1,parent2):
    def function3(self):
        print("This is a child function")
    
#main program
obj = child()
obj.function1()
obj.function2()
obj.function3()

