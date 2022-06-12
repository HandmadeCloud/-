# 18870 좌표
import numpy as np
a = int(input())
k = list(map(int,input().split()))
k2 = sorted(list(set(k)))
# print(k2)
dic = {k2[i] : i for i in range(len(k2))}
for i in k:
    print(dic[i], end = ' ')
    
# 간단한 정렬 문제인 줄 알았는데 dict 와 set을 활용해서 동률 순위를 처리하고 키에 따른 value값으로 값을 출력해버렸다..
