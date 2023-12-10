def mostCommon():
    n=int(input('zadaj cislo: '))
    t=[[n]]
    while n!=0:
        n=int(input('zadaj cislo: '))
        b=False
        for i in range(len(t)):
            if n==t[i]:
                t[i][1]+=1
                b=True
        if b==False:
            t.append(n)
        print(t)
        
    k=t[len(t):][:]
    print(k)
    return max(k)
        
#print(mostCommon())


def chop(x):
    del x[0]
    del x[len(x)-1]

t = [1, 2, 3, 4]
chop(t)
#print(t)


#scitavanie matic
def sumMat(a, b):
    if (len(a[0])==len(b[0])) and (len(a)==len(b)):     #overenie dlzky riadkov a stlpcov
        for i in range(len(a)):
            for p in range(len(b)):
                a[i][p]=a[i][p]+b[i][p]
    else:
        return 'neda sa scitat'
    return a

A=[[1,2],[3,5]]
B=[[5,2],[-3,4]]

#print(sumMat(A,B))


#nasobenie matic
def timeMat(a,b):
    t=[]
    if len(a[0])==len(b):   #overenie ze mxn a nxk => n=n
        for i in range(len(a)): #riadok
            t.append([])
            for p in range(len(b[0])):  #stlpec
                t[i].append(0)
                print(t)
                
                for n in range(len(a[0])):
                    t[i][p]=t[i][p]+a[i][n]*b[n][p]
                    
    else:
        return 'neda sa roznasobit'
    return t

A=[[1,2],[3,5],[-2,-1]]
B=[[2],[-2]]

"""A=[[1,2],[3,5],[-2,-1]]
B=[[2],[-2],[1]]"""
#print(timeMat(A,B))


def interval(t):
    maxA=t[0][0]
    minB=t[0][1]
    for i in range(len(t)):
        if t[i][0]>maxA:
            maxA=t[i][0]
        if t[i][1]<minB:
            minB=t[i][1]
    if minB-maxA>=1:
        print('(',maxA,',', minB, ')')
        return True
    else:
        return False
    
A=[[-5,4],[0,7],[3,5]]
#A=[[0,4],[2,5],[4,7]]
#print(interval(A))


def hasDuplicates(t):
    string=[str(num) for num in t]
    for i in string:
        poc=0
        for p in string:
            if i==p:
                poc+=1
            if poc>1:
                return True
    return False

print(hasDuplicates([2,3,4,5]))

print()