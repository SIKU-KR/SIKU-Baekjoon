from collections import deque

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # index 검사
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 진행 불가
            if graph[nx][ny] == 0:
                continue
            # 벽이 아니므로 이동 가능
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
print(bfs(0, 0))