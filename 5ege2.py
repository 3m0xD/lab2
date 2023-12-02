def f(N):
    n = bin(N)[2:]
    if N % 2 == 0:
        n = '1' + n + '0'
    else:
        n = '11' + n + '11'
    return int(n, 2)
N = 1
m = float('inf')
while True:
    if f(N) > 52:
        m = min(m, f(N))
        print(m)
    N += 1

