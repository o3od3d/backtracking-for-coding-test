"""
6개 수 고르기
49개중 K수 골라 집합 S만들어 그 수만 가지고 번호 선태


"""

def back(num):
    if len(res) == 6:
        print(' '.join(map(str,res)))
        return
    for i in range(num,len(S)):
        if S[i] not in res:
            res.append(S[i])
            back(i+1)
            res.pop()
while True:
    S = list(map(int,input().split()))
    K = S.pop(0)
    if K == 0:
        break
    res = []
    back(0)
    print()

