def f(N):
    n = bin(N)[2:]
    n += str(n.count('1') % 2)
    n += str(n.count('1') % 2)
    return int(n, 2)
count = 0
for N in range(1, 1000):
    if 20 <= f(N) <= 50:
        count += 1
print(count)
