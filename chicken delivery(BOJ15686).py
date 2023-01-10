"""
빈칸, 치킨, 집
치킨거리 = 집과 가장 가까운 치킨집 사이 거리
도시의 치킨거리 = 모든 집의 치킨 거리
M개의 치킨집
치킨거리가 가장작게되는
1. 아이디어
 - M개 선택하는 백트래킹, 각 치킨 집 위치 저장
 - 치킨 거리가 가장 작게되는 것
2. 시간복잡도
 - n의 수가 크기 때문에 최대한 반복 줄일 수 있는 방향

"""
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
minNum = 1e9
chicken = []
direction = [[0,1],[0,-1],[1,0],[-1,0]]
cnt = 1e9
house = []
# 집 위치 담기
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append((i,j))
        elif board[i][j] == 2:
            chicken.append((i,j))

def dfs(x,y,visit):
    global cnt
    if board[x][y] == 3:
        cnt = min(cnt,visit[x][y])
        print(1,cnt)
        return
    for dir in direction:
        nx = x + dir[0]
        ny = y + dir[1]
        if 0 <= nx < N and 0 <= ny < N:
            if visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                dfs(nx,ny,visit)
def back(num):
    global minNum
    if num == M:
        tmp = 0
        # 치킨집 거리 계산
        for x,y in house:
            cnt = 1e9
            visited = [[0] * N for _ in range(N)]
            dfs(x,y,visited)
            print(2,cnt)
            tmp += cnt
        minNum = min(minNum,tmp)
        return
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                board[i][j] = 3
                chicken.append((i,j))
                back(num+1)
                chicken.pop()
                board[i][j] = 2


back(0)
print(minNum)