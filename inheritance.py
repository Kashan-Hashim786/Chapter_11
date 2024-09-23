class employee:
  company = "Microsoft"
  def show(self):
    print(f"The name of the employee is {self.name} and the salary is {self.salary}")


class programmer(employee):
  company = "Fintech"
  def showLanguage(self):
    print(f"The name is {self.name} and he is good with {self.language} language")

employeeOject = employee()
programmerObject = programmer()

print(employeeOject.company,programmerObject.company)

