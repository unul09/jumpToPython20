# 5
n = int(input())

fibo1 = 0
fibo2 = 1
print(fibo1, end=' ')

while fibo2 <= n:
    print(fibo2, end=' ')
    temp = fibo1
    fibo1 = fibo2
    fibo2 = fibo2 + temp