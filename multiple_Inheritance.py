class employee:
  company = "Microsoft"
  salary = 125000
  def show(self):
    print(f"The name of the company is {self.company} and the salary is {self.salary}")

class coder:
  def printLanguage(self):
    print(f"Out of all the languages here is your language: {self.language}")




class programmer(employee,coder):
  company = "Fintech"
  language = "python"
  def showLanguage(self):
    print(f"The name is {self.company} and he is good with {self.language} language")

employeeOject = employee()
programmerObject = programmer()

print(employeeOject.company,programmerObject.company)
programmerObject.printLanguage()
programmerObject.show()
programmerObject.showLanguage()
