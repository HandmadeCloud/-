# 2022 03 30
a = int(input())

b = list(map(int, input().split()))

c = int(input())

d = list(map(int, input().split()))

for i in range(c):
    if d[i] in b:
        print(1)
    else:
        print(0)
        
# 테스트 결과는 정답이다. 
# 하지만 백준에서는 좀더 효율적인 정답을 요구한다.
# 시간복잡도를 생각해보면 O(n)이다.

# 좀더 효울적인 방법은 이진탐색
# 가운데를 중심으로 정렬된 수에서 가장 적합한 값을 찾아나선다.
# 탐색의 범위가 O(logn)으로 줄어들 수 있어 유용하다.
import sys
def binary_search(a,x):
    start = 0
    end = len(a) - 1 # 리스트의 특성 상
    while start < end:
        mid = (start + end) // 2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

a = int(input())

b = list(map(int, sys.stdin.readline().split()))
b.sort()
c = int(input())

d = list(map(int, sys.stdin.readline().split()))

for k in range(c):
    print(binary_search(b, d[k]))
