class calculation:
    def add(self, a:int, b:int, c:int = 0):
        print(a+b+c)

cal = calculation()
cal.add(1, 2, 3)

# method over riding

class Employee:
    __amt = 20000
    def sal(self) -> float:
        return self.__amt * 12

class contractEmployee(Employee):
    __hrpay = 1000
    __hrs = 10
    def sal(self) -> float:
        return self.__hrpay*self.__hrs
emp = contractEmployee()
print(emp.sal())

#default constructor

class Employee:
    def fullName(self, fName, lName):
        print(fName+lName)
emp= Employee()
emp.fullName("star", "akash")

# parameterless constructor

class Employee:
    def __init__(self):
        pass
    def fullName(self, fName, lName):
        print(fName+lName)
emp = Employee()
emp.fullName("naveen","alisheety")

# parameterized constructor

class Employee:
    __fName: str = " "
    __lName: str = " "
    def __init__(self, fName, lName):
        self.__fName = fName
        self.__lName = lName
    def fullName(self):
        print(self.__fName + self.__lName)
emp = Employee("shrihitha","allisheety")
emp.fullName()
