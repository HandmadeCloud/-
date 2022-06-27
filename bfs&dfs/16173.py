# 16173 점프왕 젤리 (dfs)

a = int(input())
l = []
visited = [[False]*a for i in range(a)]
for i in range(a):
    l.append(list(map(int,input().split())))

dx = [1,0]
dy = [0,1]

def dfs(x,y,visited):
    # 범위를 벗어나는 경우에 대해서 if 문을 탈출하기 위함
    if x >= a or x <= -1 or y >= a or y <= -1:
        return 0
    
    # 이미 방문한 경우인 경우 탈출
    if visited[x][y] == True:
        return 0
    
    # 맞는 경우 exit()를 사용하여 함수를 종료한다.
    if l[x][y] == -1:
        print("HaruHaru")
        exit()
    
    # 위조건들에 부합하지 않는 경우 정상적으로 방문함이 인정됨
    visited[x][y] = True
    
    # nx에는 현재 위치  +  주어진 스탯 값을 곱하여 더해주는 과정..
    # 만약에 return 0가 된다면 오른쪽 시나리오, 아래쪽 시나리오 의 방식으로 시도
    for i in range(2):
        nx = x + dx[i] * l[x][y]
        ny = y + dy[i] * l[x][y]
        dfs(nx,ny,visited)
    
    # 위에서 탈출 조건이 아닌 경우 모두 return True로 반환함
    return True

if dfs(0,0,visited)==True:
    print('Hing')
    
거의 풀지 못했다. 답을 보고 공부하게 되는 문제
사실 여기서 제대로 생각한 건 데이터 기입, 그리고 visited를 만들어주는 것 뿐이었다.
더 생각한 부분은 종료조건, 데이터의 크기를 벗어나는 경우, 그리고 진행을 위해 스탯 값을 더해주는 방법에 대해 고민한 것 뿐이었다.
각 조건에 대해서 우선순위(오류조건을 먼저 생각, 그리고 종료 조건을 생각, 방문 조건을 생각하는 것)이 있었고, 이 과정을 거친 이후에
남은 조건들 중에서 처리해주어야 하는 것(해당 지점을 방문했다는 표현)을 충분히 생각 치 못했다.
여기서는 그리고 오른쪽으로 먼저 진행할 지, 아래쪽으로 먼저 진행할 지에 대해서 nx,ny, 그리고 재귀의 방식을 사용하는신박한 표현을 내놓았다.
나는 이부분에 대해서 또다른 해답을 찾아보지 못했다.
그리고 탈출 조건에 대해서도 공부해볼 수 있는 케이스가 되었다. return 0의 활용, return 자체의 활용, exit()로 함수를 종료하는 조건등을 공부해보면서
파이썬자체를 조금 더 활용해보기 위한 노력을 할 수 있게 되었다.
