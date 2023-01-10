"""
n개 수 , n-1 연산자
주어진 수 순서는 그대로 식의 만들어
식 결과 최대와 최소 구하기

1. 아이디어
 - 모든 경우의 수를 구해야하므로 백트래킹

2. 시간복잡도
 - n

"""
maxNum = -1e9
minNum = 1e9
N = int(input())
number = list(map(int,input().split()))
oper = list(map(int,input().split()))

def operator(com,num):
    global maxNum,minNum
    if num == N:
        maxNum = max(com,maxNum)
        minNum = min(com,minNum)
        return
    if oper[0] > 0:
        oper[0] -= 1
        tmp = com + number[num]
        operator(tmp,num+1)
        oper[0] += 1
    if oper[1] > 0:
        oper[1] -= 1
        tmp = com - number[num]
        operator(tmp,num+1)
        oper[1] += 1
    if oper[2] > 0:
        oper[2] -= 1
        tmp = com * number[num]
        operator(tmp,num+1)
        oper[2] += 1
    if oper[3] > 0:
        oper[3] -= 1
        tmp = int(com / number[num])
        operator(tmp,num+1)
        oper[3] += 1

operator(number[0],1)

print(maxNum)
print(minNum)