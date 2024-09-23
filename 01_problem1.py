class D2Vector:
    def __init__(self,i,j) -> None:
        self.i = i
        self.j = j

    def show(self):
       print(f"The vector is : {self.i}i + {self.j}j")

class D3Vector(D2Vector):

 def __init__(self, i, j,k) -> None:
    super().__init__(i,j)
    self.k = k

    def show(self):
       print(f"The vector is : {self.i}i + {self.j}j + {self.k}k")

D2VectorObject = D2Vector(5,3)
D2VectorObject.show()
D3Vector_object = D3Vector(2,3,4)
D3Vector_object.show()