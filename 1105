# 2022 / 03 / 26

first, last = map(int, input().split())
k = '8'
count = 0
cnt_list = []

for i in range(first, last+1):
    for j in range(len(str(i))):
        if str(i)[j] == '8':
            count += 1
    cnt_list.append(count)
    count = 0

print(min(cnt_list))

# 개인적으로 테스트 한 결과 정답은 나온다 하지만,
# 모든 숫자의 자릿수를 하나하나 돌게하는 것으로 구현했더니 시간 초과 문제가 발생한다.
# 조금 더 효울적인 알고리즘에 대해 탐색이 필요하다.


# 참고 정답
import sys
read = lambda: sys.stdin.readline().rstrip()
L, R = read().split()
answer = 0

# 인사이트1
# 서로 자릿수가 다르다면 무조건 8이 하나도 없는 경우가 존재한다.
if len(L) != len(R):
    print(0)
else:

# 인사이트2
# 자릿수간 숫자 비교를 한다. 같은 숫자 중 동일한 문자가 있다면 그 숫자가 8인지 확인하는 과정을 진행한다.
# 자릿수간 숫자가 같지만 8이 아니라면 그냥 패스~
# 만일 동일하지 않다면, 그 아래 자리수에서 아무리 8이 많이 나와도 위가 다르므로 더이상 탐색하는 의미가 없다.

    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == '8':
                answer += 1
        else:
            break

    print(answer)
