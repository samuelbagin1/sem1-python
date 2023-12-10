import math

def moc(n,k):
    c=n
    for i in range(k-1):
        d=0
        for p in range(n):
            d = d+c
        c=d
    return c

print(moc(3,4))

print()
