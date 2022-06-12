# 단순비교로는 풀기 쉬운 문제이지만, 시간 복잡도를 줄이는 것이 가장 중요한 문제,
# 출력에는 정렬이 딱히 되어 있지 않지만 이것은 출력일 뿐, 정렬을 활용해 이진 탐색을 하여 시간 복잡도를 줄여 나가는 것이 좋다.
#10815 이진탐색
import sys

n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

card.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    # 아무것도 반환하지 않도록 하는 방법도 중요해보인다. 
    # 값을 찾았으면 mid, 아니라면 none이라는 결론으로 이어져 나중에 반환 값이 있는지 없는지 물어보는 것은 중요해 보인다.
    return None


for i in range(m):
    if binary_search(card, check[i], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
