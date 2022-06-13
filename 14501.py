a = int(input())
day = [0 for i in range(a)]
cost = [0 for i in range(a)]
ans =[0 for i in range(a+1)]
for i in range(a):
    n,m = map(int,input().split())
    day[i] =n
    cost[i] =m

    # 날짜가 넘어가는 것에 대한 처리
    if i+n > (a):
        day[i] = 0 
        cost[i] = 0

## dp 코딩 틀린부분!!!    사실 거의 다 맞췄던 것이었다..... 그래도 성장
for i in range(a-1,-1,-1):
    
        ans[i] = max(cost[i]+ans[i+day[i]],ans[i+1])
    

print(ans[0])


# 정답
n = int(input())

t_list = []
p_list = []
answer = [0] * (n + 1)

for i in range(n):
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)

for i in range(n - 1, -1, -1):
    if t_list[i] + i > n:
        answer[i] = answer[i + 1]
    else:
        answer[i] = max(p_list[i] + answer[i + t_list[i]], answer[i + 1])
        
print(answer[0])

# dp문제인 것을 인지, 뒤에서 부터 더하는 것을 인지, 하지만 for 문의 조건식을 맞춰주는 것에 대해
# 어려움을 느꼈다. 접근 방식은 #11처럼 날짜를 넘어가는 것에 대한 고려를 해주었었지만,
# 조금은 부족했던 것 같다. 새로운 ans 리스트를 만들어 누적합을 계산해보는 방법도 인지했으면
