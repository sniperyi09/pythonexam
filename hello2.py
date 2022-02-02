# 조건문
money = 2000
card = 1
if money >= 3000 and card:
    print("택시를 타고 가라")

else:
    print("걸어가리")


a = 1
b = 2

if a < b:
    print("택시를 타고 가라")

else:
    print("걸어가라")

money1 = 2000
card1 = 1
if 1  in [1,2,3]:
    print("택시를 타고 가라")
else:
    print("걸어가라")

pocket = ['paper', 'cellphone']
card2 = True
if 'money' in pocket:
    pass
elif card2:
    print("택시를 타고가라")
else:
    print("걸어가라")


score = 70
"""if score >= 60:
    message = "success"
else:
    msssage = "failure"
print(message)"""
# 3항 연산자 ?
message = "success" if score >= 60 else "failure"
print(message)

#반복문
#while문
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1 
    print("나무를 %d번 찍었습니다." % treeHit)
if treeHit == 10:
    print("나무가 넘어갑니다.")

coffee = 10
money3 = 300
while money3:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

a = 0
while a < 10:
    a = a+1
    if a % 2 == 0:
        continue
    print(a)


# for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)
    print(first)
    print(last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

marks = [90, 25, 67, 45, 70]

number = 0
for mark in marks:
    number = number +1
    if mark < 60 : continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)

sum = 0
for i in range(1,11):
    sum = sum + i
print(sum)

for i in range(2,10):
    for j in range(1,10):
        print (i*j, end =" ")
    print('')

result = [ x * y for x in range(2,10) for y in range(1,10)]
print(result)

