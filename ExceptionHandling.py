#예외처리
# try: 오루가 발샐핧 수 있는 구문
#except Exception as e: 오류발생
#else : 오류 발생하지 않음
#fanally: 무조건 마지막에 실행

#f = open("나없는파일", 'r')
#print(a)



from ast import expr_context


try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

print("배상이랑 떡친다")

try:
    f = open('none', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    print(data)
    f.close()

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
