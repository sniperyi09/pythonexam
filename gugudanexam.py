# 함수 이름은? GuGu
# 입력받는 값은? 2
# 출력하는 값은? 2,4,6,8,10....18
# 결과는 어떤 형태로? 리스트


def GuGu(n):
    result = []
    result.append(n*1)
    result.append(n*2)
    result.append(n*3)
    result.append(n*4)
    result.append(n*5)
    result.append(n*6)
    result.append(n*7)
    result.append(n*8)
    result.append(n*9)
    return result


print(GuGu(2))


def GuGu1(j):
    result = []
    i = 1
    while i < 10:
        result.append(j*i)
        i = i + 1
    return result


print(GuGu1(2))

# 3과 5의 배수 합하기
# 입력 받는 값은? 1~999(1000미만의 자연수)
# 출력하는 값은? 3의 배수와 5의 배수의 총합
# 생각해볼 것은?
# 1. 3의 배수와 5의 배수를 어떻게 찾지?
# 2. 3의배수와 5의 배수가 겹칠 때는 어떻게 찾지?

result = 0
# while n < 1000:
#   print(n)
#   n += 1

for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)


# 계시판 페이징 하기
# 함수 이름은 ? Get ToTalPage
# 입력 받는값은? 게시물의 총 건수(m), 한페이지에 보여줄 게시물의 수(n)
# 출력 하는 값은? 총페이지 수

def getTotalPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1


print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))
