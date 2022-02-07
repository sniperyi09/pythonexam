#예외처리
# try: 오루가 발샐핧 수 있는 구문
#except Exception as e: 오류발생
#else : 오류 발생하지 않음
#fanally: 무조건 마지막에 실행

#f = open("나없는파일", 'r')
#print(a)



from ast import expr_context

# 일반적인 예외처리
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

print("배상이랑 떡친다")
#else 구문
try:
    f = open('none', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    print(data)
    f.close()
#finally 구문
f= open('foo.txt', 'w')
try:
    #무언가를 실행한다.
    data = f. read()
    print(data)
except Exception as e:
    print(e)
finally:
    f.close()
    print("유연이랑 떡친다")

# 각갈 오류 처리
try:
    a=[1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱할 수 없습니다.")

try:
    f = open("나없는파일",'r')
except FileNotFoundError:
    pass
# 고의로 오류 만들기
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()
