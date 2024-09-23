class employee:
    a = 10

    @classmethod   # It will print the value of a of employee class a=10
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
  
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

object1 = employee()
object1.a = 34
object1.show()

object1.name = "laksh kumar"
print(object1.name)
print(object1.fname,object1.lname)



