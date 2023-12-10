A = [2, 5, 3, -2, -3, 0, 1]

def sucInArr(x):
    suc=0
    for i in range(len(x)):
        if i%2==0:
            suc=suc+A[i]
    return suc

#print(sucInArr(A))


A=[2, 5, 3, -2, -3, 0, -1]

def sucBigger(x):
    suc=0
    for i in range(len(x)):
        if A[i]>A[i-1] and A[i]>A[i+1]:
            suc+=1
    return suc

#print(sucBigger(A))


A=[2, 'a', [1,2], 'a', [1,2], 3]

def pocRoz(x):
    i=0
    while i<len(x):
        p=0
        poc=0
        while p<len(x):
            if x[p]==x[i]:
                poc+=1
            if poc==2:
                del x[i]
            p+=1
        i+=1
    return len(x)

#print(pocRoz(A))


A=[1, 'a', [1,2], 'a', [1,2], 3]
def ifOnetime(x):
    pocAbs=0
    for i in range(len(x)):
        poc=0
        for p in range(len(x)):
            if x[p]==x[i]:
                poc+=1
        if poc==1:
            print(x[i])
            pocAbs+=1
    return pocAbs

#print(ifOnetime(A))



#10.15 kniha prve tri ulohy
t = [[1, 2], [3], [4, 5, 6]]

def nestedSum(x):
    um=0
    for i in range(len(x)):
        um+=sum(x[i])
    return um

#print(nestedSum(t))


t = [1, 2, 3]

def cumsum(x):
    arr=[0]
    for i in range(len(x)):
        arr.append(arr[i]+x[i])
    del arr[0]
    return arr

#print(cumsum(t))


t = [1, 2, 3, 4]
def middle(x):
    del x[0]
    del x[len(x)-1]
    return x

#print(middle(t))


def isSorted(x):
    string=[str(num) for num in x]
    for i in range(len(string)-1):
        if ord(string[i])>ord(string[i+1]):
            return False
    return True

#print(isSorted([1,2,3]))
#print(isSorted(['b', 'a']))


def isAnagram(str1,str2):
    for lett1 in str1:
        b=False
        for lett2 in str2:
            if lett1==lett2:
                b=True
        if b==False:
            return False
    return True

#print(isAnagram('listen', 'silence'))


def vyhodenieFigurky(playerFigurky1, playerFigurky2):
    for poz in range(len(playerFigurky1)):
        for pozp in range(len(playerFigurky2)):
            if playerFigurky1[poz]==playerFigurky2[pozp]:
                playerFigurky2[pozp]==[-1,-1]

x=[[5,6], [5,5], [5,0], [5,3]]
y=[[5,2], [4,3], [5,5], [8,2]]

vyhodenieFigurky(x,y)
print(x,y)

print()