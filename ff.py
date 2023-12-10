def rer(n):
    if n==0:
        return 0
    else:
        return int(input('zadaj: '))+rer(n-1)
    
print(rer(5))

print()