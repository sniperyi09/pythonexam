from distutils.command.build_scripts import first_line_re


result = 0
def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

result1 = 0
result2 = 0
def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2
print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

### 클래스 ###
# 반복되는 변수 & 메서드(함수)를 미리정해놓은 틀(설계도)

class Calculator:
    def __init__(self):     #클래스를 쓰는 방법
        self.result = 0     # 1. class를 입력하고
                            # 2. 대문자로 시작하는 클래스의 이름을 작서
    def add(self, num):     # 3. 안에 들어갈 변수 설정
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

class FourCal:
    def __init__(self,first, second):
        self.first = first
        self.second = second
        pass
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add3(self):
        result = self.first + self.second
        return result

a = FourCal(3,2)
#a.setdata(4,2)
#print(a.first)
#print(a.second)
print(a.add3())


