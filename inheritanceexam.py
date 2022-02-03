### 상속 ###
class FourCal:
    def __init__(self,first, second):
        self.first = first
        self.second = second
        
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
class MoreFourCal(FourCal):
    pass

a = MoreFourCal(3,2)
print(a.add())

class FourCal1:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class SafeFourCal(FourCal1):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

b = SafeFourCal(4,0)
print(b.div())

class Family:
    lastname = "김"

Family.lastname = "박"
print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)
