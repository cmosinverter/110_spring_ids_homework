from collections import deque

def find(maze):
    
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'A':
                ra, ca = i, j
    return ra, ca

def legal(maze, r, c):
    return r >= 0 and r < len(maze) and c >= 0 and c < len(maze[0])
       

def DFS(maze, R, C):
    ra, ca = find(maze)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    vis = [[-1]*C for _ in range(R)]
    
    vis[ra][ca] = 0
    
    queue = deque([(ra, ca)])
    
    while queue:
        r, c = queue.popleft()
        
        if maze[r][c] == 'B':
            return vis[r][c]
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if legal(maze, nr, nc) and maze[nr][nc] != '#' and vis[nr][nc] == -1:
                vis[nr][nc] = vis[r][c] + 1
                queue.append((nr, nc))
            
    return -1
                
    


R, C = map(int, input().split())
maze = [list(input()) for _ in range(R)]
dis = DFS(maze, R, C)
    
print(dis if dis != -1 else 'IMPOSSIBLE')
