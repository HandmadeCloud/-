# 1388번
n,m = map(int, input().split())
l = []
cnt = 0
for _ in range(n):
    l.append(list(input()))

for i in range(n):
    chk = '1'
    for j in range(m):
        if l[i][j] == '-':
            if l[i][j] != chk : # 비교하는 수를 변수처럼 변화토록 한다.
                cnt += 1
        chk = l[i][j]
for j in range(m):
    chk = '1'
    for i in range(n):
        if l[i][j] == '|':
            if l[i][j] != chk : 
                cnt += 1
        chk = l[i][j]
print(cnt)

# 행별로 경우의 수와 열별로 경우의 수를 구분해서 생각해야 하는 문제
# 처음 chk에 아무 값을 넣어주고 이후 비교하게 될 값을 넣어주며 비교를 하는 변수 역할을 하도록 한다.
# 중복체킹을 방지하는 역할을 하지 않을까라고 생각
# 대부분의 내가 생각한 코드와 비슷했지만 이러한 변수 활용 능력을 키워야 한다고 생각...
