
# 내장 함수
# 라이브러리에서 가져다 쓰는 함수
print(dir([1, 2, 3, ]))


def positive(x):
    return x > 0


a = list(filter(positive, [1, -3, 2, 0, -5, 6]))
print(a)


def two_times(x):
    return x*2


b = list(map(two_times, [1, 2, 3, 4]))
print(b)

c = list(map(lambda a: a*2, [1, 2, 3, 4]))
print(c)
