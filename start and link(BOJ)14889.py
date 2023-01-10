"""
N은 짝수
N/2 스타트 팀 링크팀
i,j 더했을때 능력치 SIJ SJI
스타트와 링크 팀 능력치 차이 최소

1. 아이디어
 - 모두 확인위해 백트래킹

2. 시간복잡도

3. 자료구조

"""

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
direction = [[0,1],[0,-1],[1,0],[-1,0]]
minNum = 1e9
visited = [False] * N

def back(num,idx):
    global minNum
    if num == N//2:
        startSum = 0
        linkSum = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    startSum += board[i][j]
                elif not visited[i] and not visited[j]:
                    linkSum += board[i][j]
        minNum = min(minNum,abs(startSum-linkSum))
        return

    for i in range(idx,N):
        if not visited[i]:
            visited[i] = True
            back(num+1,i+1)
            visited[i] = False
back(0,0)
print(minNum)


