"""
1. 아이디어
 - 백트래킹 재귀함수를 FOR 돌면서 숫자 선택 (방문여부 확인)

2. 시간복잡도
 - N! = 8! < 2 억 가능

3. 자료구조
 - 결과값

"""
N,M = map(int,input().split())
res = []

def back(num):
    if len(res) == M:
        print(' '.join(map(str,res)))
        return
    for i in range(num,N+1):
        if i not in res:
            res.append(i)
            back(i+1)
            res.remove(i)
back(1)