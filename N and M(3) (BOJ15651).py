N,M = map(int,input().split())
res = []

def back(num):
    if num == M:
        print(' '.join(map(str,res)))
        return
    for i in range(1,N+1):
        res.append(i)
        back(num+1)
        res.pop()
back(0)
