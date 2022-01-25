from platform import python_build


print("hello, world")

a = "I eat %d apples." % 3 


print(a)

b= "hobby"

print(b.count('b'))

c = "Life is too short"
print(c.replace("Life", "Your leg"))
d = "Life is too short"
print(d.split())
#리스트
e = [ "이시영", "김정현","배상이","김유리","정유연","홍유리"]
e[0] = "석주현"
e[1] = "서현숙"
e.append("손민지")
e.sort()
e.reverse()
e.insert(0,"한주희")
print(e)
#튜플 
t1 = ("신유빈", "장원영", "김은지", "유영")

print(t1)
# 딕셔러니
dic = {'name':'eric', 'name1':'상이'}
print(dic)
print(dic.keys())
print(dic.values())
for f, g in dic.items():
    print("키는:" + f)
    print("벨류는:"+ g)
    print(dic.get("name1"))

#집합
s1 = set([1,2,3])
s1 = {1,2,3}
print(type(s1))
#집합은 데이터 분야에서 많이씀
#교집합

s2 = set([1,2,3,4,5,6,7,8,9])
s3 = set([3,4,5,7,8,6])
print(s2& s3)
print(s1.intersection(s2))
print(s1|s2)
print(s2.union(s3))
print( s2 - s1)