# 외장함수

import time
import random
import webbrowser

print(time.time())

for i in range(5):
    print(i)
   # time.sleep(1)


random.randint(1, 10)
print(random.random())

lotto = sorted(random.sample(range(1, 46), 6))
print(lotto)

webbrowser.open("http://google.com")
