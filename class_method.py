class employee:
    a = 10

    @classmethod   # It will print the value of a of employee class a=10
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

object1 = employee()
object1.a = 34
object1.show()




