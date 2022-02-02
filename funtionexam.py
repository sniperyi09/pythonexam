def sum(a,b):
    result = a + b
    return result
print(sum(1,2))

def say():
    return 'hi'
print(say())

def sum1(a,b):
    print("%d, %d의 합은 %d입니다" % (a,b,a+b))

sum1(1,2)
print(sum1(1,2))

myList = [1,2,3]
#print(myList.append(4))
print(myList.pop())
print(myList)

def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(sum_many(1,2,3))

def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if(k=="name"):
            print("당신의 이름은 : " + kwargs[k])
print(print_kwargs(name="1", b="2"))

def sum_and_mul(a,b):
    return a+b, a*b, a-b
print(sum_and_mul(1,2))

def say_myself(name,old,man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다."  % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("배상이", 35, False)

a = 1
def vartest(a):
    a = a + 1
    return a
a = vartest(a)
print(a)

b = 1
def vartest1():
    global b
    b = b + 1

vartest1()
print(b)

#일반 함수
def add(a,b):
    return a+b

#lambda 표현식
#add = lambda a, b: a+b
print(add(1,2))

#myList1 = [lambda a,b: a+b, lambda a,b: a*b]
#print(myList1[0](1,2))

#number = input("숫자를 입력하세요:")

#print(number)

print("배상이" "정유연" "홍유리" "김유리")
print("상이야", "사랑해","사귀자")

for i in range(10):
    print(i, end=' ')


f = open("새파일.txt", 'w', encoding = "UTF-8")
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.write("배상이와 결혼하고 애 낳고 잘살거임!!")
f.close()

d = open("새파일.txt", 'r', encoding ="UTF-8")
while True: 
    line = d.readline()
    if not line: break
    print(line)

for line in line:
    print(line.strip("\n"), end = " ")
d.close()

e = open("새파일.txt", 'r', encoding ="UTF-8")
lines = e.readlines()
for line in lines:
    print(line.strip("\n"), end = " ")
e.close()




h = open("새파일.txt", 'a', encoding ="UTF-8")
for i in range(11,20):
    data = "%d번째 줄입니다.\n" % i
    h.write(data)
h.write("정유연하고 잘거다")
h.close()

g = open("새파일.txt", 'r', encoding = "UTF-8")
data = g.read()
print(data)
g.close()

###### Immutable ######
a = 1
def vartest(a):
    a = a + 1
vartest(a)
print(a)

#########################

######  mutable  ######
b = [1,2,3]
def vartest(b):
    b = b.append(4)
vartest(b)
print(b)