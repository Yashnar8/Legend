K, N = map(int, input().split())
A = list(map(int, input().split()))
SL = sorted(A, reverse=True) 
B = 0
C = 0
for i in SL:
    B += i
    C += 1
    if B >= K:
        break
print(C)
