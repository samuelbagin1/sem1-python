def sucN(n): #1.
    if n==0:
        return 0
    else:
        return n+sucN(n-1)

#print(sucN(10))


def sucP(n):    #2.
    if n==1:
        return int(input('zadaj cislo: '))
    else:
        return int(input('zadaj cislo: '))+sucP(n-1)

#p=int(input('zadaj pocet cisel kt chces nacitat: '))
#print(sucP(p))


def sucParnych(n):  #sucet parnych
    if n==1:
        k=int(input('zadaj cislo: '))
        if k%2==0:
            return k
        else:
            return 0
    else:
        k=int(input('zadaj cislo: '))
        if k%2==0:
            return k+sucParnych(n-1)
        else:
            return sucParnych(n-1)

#p=int(input('zadaj pocet cisel kt chces nacitat: '))
#print(sucParnych(p))



def pocParnych(n):  #3. pocet parnych
    if n==1:
        k=int(input('zadaj cislo: '))
        if k%2==0:
            return 1
        else:
            return 0
    else:
        k=int(input('zadaj cislo: '))
        if k%2==0:
            return 1+pocParnych(n-1)
        else:
            return pocParnych(n-1)

#p=int(input('zadaj pocet cisel kt chces nacitat: '))
#print(pocParnych(p))


def najMax(n,max):  #4.
    if n==1:
        k=int(input('zadaj cislo: '))
        if k>max:
            return k
        else:
            return max
    else:
        k=int(input('zadaj cislo: '))
        if k>max:
            max=k
            return najMax(n-1, max)
        else:
            return najMax(n-1, max)
                
#p=int(input('zadaj pocet cisel kt chces nacitat: '))
#print(najMax(p,0))


def parSuc(n, b):   #5.
    if n==1:
        k=int(input('zadaj cislo: '))
        if (b==True and k%2==0) or (b==False and k%2==1):
            return True
        else:
            return False
    else:
        k=int(input('zadaj cislo: '))
        if (b==True and k%2==0) or (b==False and k%2==1):
            return parSuc(n-1, True)
        else:
            return parSuc(n-1, False)
        
#p=int(input('zadaj pocet cisel kt chces nacitat: '))
#print(parSuc(p,True))


def testPrvoCis(c):
    testPrvoCis=True
    for i in range(2,c):
        if c%i==0:
            testPrvoCis=False
    return testPrvoCis

def sucPrvo(n): #6., checkujeme ci su cisla prvocila po n (NIE CI SA CISLO ROVNA N), v testPrvoCis checkujeme n-1 a vraciame s -1
    if n==1:
        return -1
    else:
        if testPrvoCis(n-1)==True:
            print(n)
            return n-1+sucPrvo(n-1)
        else:
            return sucPrvo(n-1)

#print(sucPrvo(17))

print()

