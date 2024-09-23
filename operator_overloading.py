class Number:
    def __init__(self,n) -> None:
        self.n = n

    def __add__(self,num):
        return self.n + num.n
    def __sub__(self,num):
        return self.n - num.n
    def __mul__(self,num):
        return self.n * num.n
    
n = Number(1)
m = Number(3)

print(n+m)
print(n-m)
print(n * m)