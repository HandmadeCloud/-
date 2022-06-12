#1012 유기농 배추
#bfs인 것을 알고 풀어보려고 노력했지만, 인접값 처리를 어떻게 해야할 지 몰라 틀림


a = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1] 
        del queue[0] # a,b만 구하고 이전 큐는 지운다 결국 큐는 비어있게 됨
        # 동서남북 탐색과정
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            # 범위를 벗어나지 않는 지 체크, 인접한 행렬이 있는 지 탐색
            if 0 <= q < n and 0 <= w < m and l[q][w] == 1:
                # 탐색한 값은 0으로 바꾸고
                l[q][w] = 0
                
                # 있다고 탐지된 값을 또 인접한 탐색을 이어갈 수 있도록 값을 큐에 추가하게 됨
                # 다시 while 문을 이어갈 수 있는 수단~
                queue.append([q, w])

for _ in range(a):
  
    # 배추 크기 입력
    m,n,k = map(int,input().split())
    # 길이만 큼 0 리스트를 먼저 생성해준다.
    l = [[0] * m for i in range(n)]
    
    # 배추가 어디 위치에 있는 지 입력
    for _ in range(k):
        x,y = map(int,input().split())
        l[y][x] = 1
    cnt = 0
    
    # 탐색 과정을 들어간다.
    for q in range(n):
        for w in range(m):
            if l[q][w] == 1:
                bfs(q, w)
                # 탐색이 끝난 후 0으로 바꿔준다.
                l[q][w] = 0
                cnt += 1
print(cnt)

# bfs 문제인데 아직은 어렵게 느껴지는 부분이 많다. 기존의 구현 문제에서 조금 더 생각해야 하는 부분들이 많아서
# 조금 더 폭넓게 생각하고 문제를 풀어나가야할 것 같다. bfs,dfs,그리고 deque, queue, stack 등 이정도 시나리오는 생각하고
# 알고리즘 풀이에 접근하는 것이 좋은 방법일 듯 하다.
