import sys
input = sys.stdin.readline

N, M = map(int,input().split()) 
trees = list(map(int, input().split()))

start, end = 0, max(trees) 

# 이분 탐색
while start <= end:
    mid = (start+end)//2
    tree = 0
    for i in trees:
        if i > mid:
            tree += i - mid

    if tree >= M: # 원하는 나무 높이보다 더 많이 잘렸으면
        start = mid + 1
    else: # 원하는 나무 높이보다 덜 잘렸으면
        end = mid - 1
print(end)

# 이분 탐색에 대해 다루고 있다.
# 처음 생각했던 건 입력한 trees 값들 중 중간 값에서 부터 위아래로 탐색하면 좋겠다고 생각했는데,
# 그럴 경우 중간값보다 큰 경우 최소값이 아니더라도 출력이 되는 경우가 발생했다.
# 그래서 고민을 해보다 참고 답안을 확인하게 되었는데 더 참신한 답변이 아닌 익숙한 답안이었다.
# 단순한 이분 탐색을 진행했지만 내가 생각했던 것과 차이가 있었다..
# start를 입력값의 최소가 아닌 0부터, 그리고 최대값 까지 그리고 while문은 start 가 end를 넘어서면 break되도록
# 이부분이 가장  큰 차이였던 것 같다. 단순히 while True는 아닐 것이라고 생각했는데 딱히 마땅한  생각이 떠오르지 않았다.
# mid를 구해주고 겨로가에  따라 mid를 조절하는 방법은 내가 생각했던 것과 동일했다.
# 이분탐색을 조금더 야만적인(?) 노가다 방법부터 생각하면서 더 효율적인 방법을 강구해보는 것이 좋을 것같다.
# 하지만 완전 처음부터 아주 단순한 노가다를 하지 않고 더 방법을 찾기 위했음에 의의를 두자.. 좀더 좋아질 것 같다.
