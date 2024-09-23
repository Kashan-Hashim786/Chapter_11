class complex:
    def __init__(self,r,i) -> None:
        self.r = r
        self.i = i

    def __add__(self,c2):
        return complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self,c2):
        real_part = self.r * c2.r - self.i * c2.i
        img_part = self.r * c2.i + self.i * c2.r
        return complex(real_part,img_part)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
object1 = complex(1,2)
object2 = complex(3,4)

print(object1 + object2)
print(object1 * object2)

