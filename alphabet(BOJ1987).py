"""

"""

R,C = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(R)]
res = set()
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
maxNum = 0
def back(x,y,cnt):
    global maxNum
    res.add(board[x][y])
    maxNum = max(maxNum,cnt)
    for i in range(4):
        nx,ny = x + dx[i],y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if board[nx][ny] not in res:
                back(nx,ny,cnt+1)
    res.remove(board[x][y])
back(0,0,1)
print(maxNum)