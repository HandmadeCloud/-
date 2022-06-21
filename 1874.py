a = int(input())
s = []
ans = []
cnt = 1
temp = True
for i in range(a):
    num = int(input())
    while cnt <= num:
        s.append(cnt)
        ans.append('+')
        cnt += 1
    if s[-1] == num:
        s.pop()
        ans.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in ans:
        print(i)
# cnt로 처리하면 될 걸 어렵게 리스트로 만들어서 해결하려 했던 것이 문제..
# 그렇게 생각치 못했떤 이유..4 3 이 뽑였다면 5 6 으로 진행하면 될 것을 앞번호 진행을 계속 신경쓰느라 리스트로 만들어 포문으로 해결하려고함
# while문 한줄을 생각했다면 이럴 일은 없었을 것
