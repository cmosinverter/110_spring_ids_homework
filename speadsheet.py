from collections import deque

n, m = map(int, input().split())
val = [0]*(n+1)
indeg = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for i in range(m):
    cmd = list(map(int, input().split()[1:]))
    index = cmd[0]
    val[index] = cmd[-1]
    for node in cmd[1:-1]:
        graph[node].append(index)
        indeg[index] += 1

q = deque([x for x in range(1, n+1) if indeg[x] == 0])

while q:
    u = q.popleft()
    for neighbor in graph[u]:
        indeg[neighbor] -= 1
        val[neighbor] += val[u]
        if indeg[neighbor] == 0:
            q.append(neighbor)
            
for i in range(1, n+1):
    print(val[i] if indeg[i]==0 else '#REF!')
