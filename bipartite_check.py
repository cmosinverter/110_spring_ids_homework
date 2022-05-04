from collections import deque


def BipartiteCheck(graph):
    
    color = {}
    q = deque([])
    
    for i in range(1, v+1):
        if i not in color:
            q.append(i) ## '1' for red '-1' for blue
            color[i] = 1
            
        while(q):
            node = q.popleft()
            for neighbor in graph[node]:
                if neighbor in color:
                    if color[neighbor] == color[node]:
                        return False
                else:
                    q.append(neighbor)
                    color[neighbor] = color[node]*(-1)
                    
        return True
                    

v, e = map(int, input().split())
adj = [[] for i in range (v+1)]
for i in range(e):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
        
print('YES' if BipartiteCheck(adj) else 'NO')
