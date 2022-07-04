n = int(input())
chon = list(map(int,input().split()))
m = int(input())

visited = [False] * (n+1)
res = [0]*(n+1)
l = [[] for _ in range(n+1)]

for i in range(m):
    k = list(map(int,input().split()))
    l[k[0]].append(k[1])
    l[k[1]].append(k[0])

cnt = 1

def dfs(v):
    visited[v] = True
    for i in l[v]:
        if not visited[i]:
            res[i] = res[v] + 1
            dfs(i)
        
            
dfs(chon[0])

if res[chon[1]]>0:
    print(res[chon[1]])
else:
    print(-1)
