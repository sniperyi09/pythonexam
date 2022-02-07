### 모듈이란? ###
#미리 만들어 놓은 .py파일(함수, 변수, 클래스)
#all import
#import mod1
#print(mod1.add(1,2))

#특정 함수만 호출
#from mod1 import sub
#print(sub(3,2))


import sys
sys.path.append("D:\\jocoding\\second")

import mod2
print(mod2.add(3,4))

