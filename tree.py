from collections import deque, defaultdict
n = int(input())
nums = list(map(int, input().split()))
graph = [[] for i in range(n)]
for i in range(n-1):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    graph[u].append(v)
    graph[v].append(u)
    
q = deque([(0, 0)]) #(index, distance from root to node)
vis = set()
dist = {}
while q: # construct a table to determine children and parent
    u, dis = q.popleft()
    vis.add(u)
    dist[u] = dis
    for nei in graph[u]:
        if nei not in vis:
            q.append((nei, dis+1))
            vis.add(nei)

sums = [0]*n
first_stack, second_stack = [0], []

while first_stack: # iterative DFS on the graph
    cur = first_stack.pop()
    second_stack.append(cur)
    for nei in graph[cur]:
        if dist[nei]>dist[cur]:
            first_stack.append(nei)
while second_stack: #add the value from bottom to top
    cur = second_stack.pop()
    tmp = nums[cur]
    for nei in graph[cur]:
        if dist[nei]>dist[cur]:
            tmp += sums[nei]
    sums[cur] = tmp
print(' '.join(map(str, sums)))
