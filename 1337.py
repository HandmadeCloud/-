# 1337
a = int(input())
l = []
cnt = 0
ans = []
for _ in range(a):
    k = int(input())
    l.append(k)
for i in range(a):
    for j in range(1,len(l)):
      # 연속성을 이렇게 판정 다음 값이 리스트에 있는가
        if l[i] + j in l:
            pass
      # 없을 경우 추가되어야 하는 숫자 추가
        else:
            cnt += 1
    # 그렇게 값별로 필요한 숫자를 정답 리스트에 추가함
    ans.append(cnt)
    cnt = 0
    
# 그 중에서 가장 작은 값을 출력함
print(min(ans))

# 아무것도 참고하지 않은 채 오로지 혼자 풀었던 문제! 조금씩 생각이 발전하고 있음을 느낀다 ㅎㅎ
