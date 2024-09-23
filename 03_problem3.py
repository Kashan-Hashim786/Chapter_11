class employee:
    salary = 234
    increment = 0.2
    
    @property
    def salaryAfterIncrement(self):
     return (self.salary + (self.salary * self.increment))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
      self.increment = ((salary/self.salary) - 1 ) * 100

e = employee()
e.salaryAfterIncrement = 280
print(e.increment)