# 22/03/29
n,m = map(int,input().split())
l = []
for poketmon in range(n):
    poketmon = input()
    l.append(poketmon)
    
for search in range(m):
    search = input()
    if search in l:
        print(l.index(search))
    else:
        search = int(search)
        print(l[search])
# 데이터를 받아서 리스트에 정리하고
# 리스트에서 문자가 온다면 리스트에서 탐색토록 하고,
# 숫자가 온다면 해당하는 저장된 리스트에서 해당하는 포켓몬을 출력하도록 했다.
# 테스트 결과 정상적으로 작동하였다.
# 하지만 시간초과나 효율성 문제에서 다소 부족한 면이 많았음

# 참고답안
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])
        
# 주어진 내용을 dict에 저장하도록 했다. 여태 리스트만 생각하고 이것에만 집중한 나머지 더 편한방법을 생각하지 못함
# 주어진 내용을 dict에 번호:이름, 이름:번호로 한번씩 저장한다. 그리고 들어오는 내용이 숫자인지 문자인지를 판단하여
# 딕셔너리에서 찾아서 출력해주도록 한다.
