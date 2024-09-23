class employee:
    def __init__(self) -> None:
        print("The constructor of employee")
    a = 1

class programmer(employee):
     def __init__(self) -> None:
        print("The constructor of programmer")
     b = 2

class manager(programmer):
     
     def __init__(self)  -> None:
        super().__init__()
        print("The constructor of manager")
     c = 3
'''
object3 = programmer()
print(object3.a)



object2 = programmer() # The programer can access all the features of employe class 
print(object2.a,object2.b)
'''

object1 = manager() # the manager class can access all the feature of both classes "employee and programmer"
print(object1.a,object1.b,object1.c)
