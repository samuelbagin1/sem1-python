def row(n):
    print()
    print('+', end='')
    for i in range(n):
        print(' - - - - +', end='')

def col(n):
    for i in range(4):
        print()
        print('?', end='')
        for p in range(n):
            print('         ?', end='')

def grid(k):
    for t in range(k):
        row(k)
        col(k)
    row(k)
        

#grid(3)


def malNas():
    for i in range(10):
        for p in range(10):
            print((i+1)*(p+1), end=' ')
        print()

malNas()

print()

def od1poN(n):
    for i in range(n+1):
        for p in range(i):
            print(p+1, end=' ')
        print()

od1poN(5)

for i in range(6):
    print(6-i)
    
print()