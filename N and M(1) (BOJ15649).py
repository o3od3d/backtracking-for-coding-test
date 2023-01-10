"""

1. 아이디어
 - 백트래킹 재귀함수 안에서, FOR 돌면서 숫자 선택(이때 방문 여부 확인)
 - 재귀함수에서 m개를 선택할 경우 print

2. 시간복잡도
 - N! < 2억 가능
 - N = 8

3. 자료구조
 - 결과값 저장 INT[]
 - 방문 여부 체크 INT[]
"""
N,M = map(int,input().split())
visited = [False] * (N+1)
res = []

def backtracking(num):
    if num == M:
        print(' '.join(map(str,res)))
        return
    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = True
            res.append(i)
            backtracking(num+1)
            visited[i] = False
            res.pop()

backtracking(0)