# 1138 한 줄로 서기
a = int(input())
l = [0] * a
cnt = 0
k = list(map(int,input().split()))
for i in range(a):
    cnt = k[i]
    while True:
        if l[cnt] == 0:
            l[cnt] = i+1
            break
        else:
            cnt += 1
for i in range(a):
    print(l[i],end = ' ')

#6 
#6 1 1 1 2 0 0입력시
# 6 2 3 4 5 7 1 로 출력의 위치가 잘못 되었다.. 자기 자리에 위치할 수 있도록 조정이 필요했다
    
# 풀이    
n = int(input())
s = list(map(int, input().split()))
a = [0 for i in range(n)]
for i in range(n + 1):
    count = 0
    k = s[i - 1]
    for j in range(0, n):
        if count == k and a[j] == 0:
            a[j] = i
            break
        if a[j] == 0:
            count += 1
for b in a:
    print(b, end = ' ')
    
# 여러 테스트 케이스는 맞췄지만 마지막 케이스에 대해 틀려 어떤 부분이 문제인지는 인지했지만 
# 어떻게 바궈야 할 지 몰라 멈췄던 문제
# #29의 count==k 처럼 자기 입력값이 곧 위치값인 경우의 수를 추가해주었다면 쉽게 맞췄을 것 같다..1
