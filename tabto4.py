# 탭을 4개의 공백으로 바꾸기
# 필요한 기능은? 문서 파일 읽어들이기, 문자열 변경하기
# 입력받는 값은? 탭을 포함한 문서파일
# 출력하는 값은? 탭이 공백으로 수정된 문서 파일
# python tabto4.py a.txt b.txt

import sys

src = sys.argv[1]
dst = sys.argv[2]

print(src)
print(dst)
