n,m = map(int,input().split())
res = []

def back(num):
    if len(res) == m:
        print(' '.join(map(str,res)))
        return
    for i in range(num,n+1):
        res.append(i)
        back(i)
        res.pop()
back(1)