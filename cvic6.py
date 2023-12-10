def sucInput(): #1.
    sucInput=-1
    n=1
    while n>0:
        sucInput=sucInput+n
        n=int(input('zadaj cislo: '))
    return sucInput

#print(sucInput())


def isStvorec(n):   #2.
    prirCis=0
    while prirCis**2<n:
        print(prirCis**2)
        prirCis+=1

#isStvorec(17)


def prirCisX(n):    #3.
    x=0
    prirCisX=1
    while prirCisX*2<n:
        prirCisX=prirCisX*2
        x+=1
    return x

#print(prirCisX(32))


def inpCis():   #4.
    inpCis=1
    x=int(input('zadaj cislo: '))
    max=x
    while x!=0:
        x=int(input('zadaj cislo: '))
        if x>max and x!=0: 
            inpCis+=1
            max=x
    return inpCis

#print(inpCis())


def cisPredMax():   #5.
    x=int(input('zadaj cislo: '))
    cisPredMax=x
    poc=0
    while x!=0:
        x=int(input('zadaj cislo: '))
        if x>cisPredMax: 
            poc+=1
        cisPredMax=x
    return poc

#print(cisPredMax())


def pocNaj():   #6.
    A=[]
    A.append(int(input('zadaj cislo: ')))
    max=A[0]
    i=0
    while A[i]!=0:
        A.append(int(input('zadaj cislo: ')))
        if A[i]>max: 
            max=A[i]
        i+=1
    pocNaj=0
    for p in range(0,i):
        if A[p]==max:
            pocNaj+=1
    return pocNaj

#print(pocNaj())


def postRov():
    x=int(input('zadaj cislo: '))
    preX=x
    postRov=1
    maxPostRov=0
    while x!=0:
        x=int(input('zadaj cislo: '))
        if preX==x:
            postRov+=1
        if postRov>=maxPostRov:
            maxPostRov=postRov
        if preX!=x:
            postRov=1
        preX=x
    return maxPostRov

#print(postRov())


def fibonacci(n):
    if n==0:
        return 0
    elif  n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
def ifFib(x):
    n=20
    while n!=-1:
        if x==fibonacci(n):
            break
        n=n-1
    return n

#print(ifFib(13))


import math
def testSquareRoot(a):
    x=5
    while True:
        y = (x + a/x) / 2
        if y == x:
            break 
        x=y
    return x

print('a           mysqrt(a)        math.sqrt(a)    diff')
for pp in range(1,10):
    print(pp, '         ', testSquareRoot(pp), '            ', math.sqrt(pp), '    ', )

print()