a = int(input())
hotel_list = []
for i in range(a):
    h,w,n = map(int,input().split())
    for j in range(1,w):
        if j < 10:
                j = '0'+str(j)
        for k in range(1,h+1):
            num = str(k)+str(j)
            hotel_list.append(num)
    print(hotel_list[n-1])
    hotel_list = []
    
#모든 층을 탐색하는 과정 호수를 집어 넣기 위해 다양한 노력을 했응
#코드를 테스트 해본 결과는 맞지만, 런타임에러


# 참고정답
t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    f = 0
    ho = 0
    # 찾고자 하는 수를 층으로 나누었을 때 나머지가 0이라면,
    # 해당 층에 그리고 해당하는 몫(즉, 1) 이 위치하게 된다.
    # 10층에 10번째 값일 경우 1001호가 자연스럽게 완성
    if n % h == 0:
        f = h * 100
        ho = n // h
    else:
      # 거의 대부분의 경우는 이 경우. 나머지 만큼의 층 수,
      # 몫 만큼 + 1 의 값이 호수로 완성..
        f = (n % h) * 100
        ho = 1 + n // h
    print(f + ho)
 
# 노가다로 한 코딩과 // 창의적인 코딩방법의 차이를 많이느낌
# 브론즈 문제라지만 다양한 시도를 먼저 해본 후에 코딩을 해야 한다는 점을 계속 느끼게 된다.
