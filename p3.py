# 프로젝트 문제 3번
from collections import deque

input = [[4, 3, 2, 1],
         [0, 0, 0, 0],
         [0, 0, 9, 0],
         [1, 2, 3, 4]]
N = 4

forest = []

def problem3(input):
    bear_size = 2
    honeycomb_count = 0
    time = 0
    bear_x, bear_y = 0, 0
    # 입력 힌트

    # forest 리스트를 input 리스트로 초기화
    forest = [row[:] for row in input]
    
    # 곰의 초기 위치 찾기
    for i in range(N):
        for j in range(N):
            if forest[i][j] == 9:
                bear_x, bear_y = i, j
                forest[i][j] = 0

    def bfs(x,y):
        visited=[[False] * N for _ in range(N)]
        queue = deque([(x,y,0)])
        visited[x][y] = True
        honeycombs = []

        while queue:
            cx, cy, dist = queue.popleft()
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx,ny = cx+dx,cy+dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if forest[nx][ny] <= bear_size:
                        visited[nx][ny] = True
                        if forest[nx][ny] != 0 and forest[nx][ny] < bear_size:
                            honeycombs.append((dist+1,nx,ny))
                        queue.append((nx,ny,dist+1))
        return sorted(honeycombs, key=lambda x:(x[0],x[1],x[2]))
                        
    while True:
        honeycombs = bfs(bear_x,bear_y)
        if not honeycombs:
            break

        dist, honey_x, honey_y = honeycombs[0]
        time += dist
        bear_x, bear_y = honey_x, honey_y
        honeycomb_count += 1
        forest[bear_x][bear_y] = 0

        if honeycomb_count == bear_size:
            bear_size += 1
            honeycomb_count = 0

        
    return time

result = problem3(input)

assert result == 14
print("정답입니다.")
