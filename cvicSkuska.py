#ulohy su z PROG1_cvicne_priklady_T9azT10.pdf

def F(zoznam):
    for retazec in zoznam:
        for znak in retazec:
            if znak=='a':
                return retazec
            
A=['jfr', 'sufhu', 'fjdbgnhd', 'saz', 'hdgfbuidj', 'sazmvkf']
#print(F(A))


def F1(zoznam):
    string=''
    for retazec in zoznam:
        string+=retazec[0]
    return string

#print(F1(A))


def notRepeating(t):
    pocNeopak=0
    for retazec in t:
        doNotCount=False
        for znak in retazec:
            pocZnakov=0
            for znak1 in retazec:
                if znak==znak1:
                    pocZnakov+=1
                if pocZnakov==2:
                    doNotCount=True
        if doNotCount==False:
            pocNeopak+=1
    return pocNeopak

A=['asd', 'ddf', 'rtyuiok', 'ertyu', 'dfjnk', 'fgshdd', 'fkcckkk', 'rtyuiop']
#print(notRepeating(A))


def F2(t):
    maxLength=len(t[0])
    maxRet=t[0]
    for retazec in t:
        doNotCount=False
        for znak in retazec:
            pocZnak=0
            for znak1 in retazec:
                if znak==znak1:
                    pocZnak+=1
            if pocZnak>=2:
                doNotCount=True
        if doNotCount==False and maxLength<len(retazec):
            maxRet=retazec
            maxLength=len(retazec)
    return maxRet

print(F2(A))


#sekcia 2: nacitavanie do zoznamu
def writeInNumb(k):
    t=[]
    suc=0
    while suc<=k:
        t.append(int(input()))
        suc=sum(t)
    return t

#s=int(input())
#print(writeInNumb(s))


def writeInNumb1(n):
    t=[]
    b=False
    while b==False:
        k=int(input())
        for i in t:
            if k==i:
                b=True
        if b==False:
            t.append(k)
    return t

#s=int(input())
#print(writeInNumb1(s))


def rozsah1(n):     #rozsah mysleny ako rozdiel najvacsieho cisla a najmensieho
    b=False
    t=[]
    while b==False:
        t.append(int(input()))
        if t[len(t)-1]-t[0]>n:
            b=True
    return t

#print(rozsah1(20))

def rozsah2(n):     #rozsah mysleny ako rozdiel najvacsieho a najmensieho indexu
    b=False
    t=[]
    while b==False:
        t.append(int(input()))
        if len(t)>n:
            b=True
    return t


def pocRozCisel(n):
    b=False
    t=[]
    rozCisla=[]
    while b==False:
        k=int(input())

        overenie=False
        for i in t:
            if i==k:
                overenie=True
        if overenie==False:
            rozCisla.append(k)
        
        t.append(k)
        
        if len(rozCisla)>=n:
            b=True
    return t

#print(pocRozCisel(3))


#sekcia 3: matice
def matFind(A, x):
    for i in range(len(A)):
        for p in A[i]:
            if p==x:
                return True
    return False

matica=[[1,5], [2,6], [3,8], [10,4], [2,2], [1,11], [3,5]]
#print(matFind(matica, 2))


def matFindPoc(A, x):
    poc=0
    for i in range(len(A)):
        for p in A[i]:
            if p==x:
                poc+=1
    return poc

#print(matFindPoc(matica,2))


def matFindMax(A):
    maximum=A[0][0]
    for i in range(len(A)):
        if max(A[i])>maximum:
            maximum=max(A[i])
    return maximum

#print(matFindMax(matica))


def matFindMaxInd(A):
    maximum=A[0][0]
    pozicia=[0,0]
    for i in range(len(A)):
        if max(A[i])>maximum:
            maximum=max(A[i])
            pozicia=[i, A[i].index(maximum)]
    return pozicia

#print(matFindMaxInd(matica))


def sameNuly(A):
    pocNul=0
    for p in range(len(A[0])):  #stlpec
        bRiadok=True
        for i in range(len(A)): #riadok
            if A[i][p]!=0:
                bRiadok=False
        if bRiadok==True:
            pocNul+=1
    return pocNul

matica1=[[0,0,1], [0,0,1], [0,0,1], [0,0,1], [0,0,1], [0,0,1]]
#print(sameNuly(matica1))


def ifRovnake(A):
    for p in range(len(A[0])):  #stlpec
        bRiadok=True
        for i in range(len(A)): #riadok
            if A[i][p]!=A[0][p]:
                bRiadok=False
        if bRiadok==True:
            return True
    return False

#print(ifRovnake(matica1))


def ifRoznyStlpec(A):
    for p in range(len(A[0])):  #stlpec
        bRiadok=True
        for i in range(len(A)): #riadok
            poc=0
            for ii in range(len(A)):
                if A[ii][p]==A[i][p]:
                    poc+=1
            if poc==1:
                return True
    return False

#print(ifRoznyStlpec(matica1))


def indexMaxStlpca(A):
    for p in range(len(A[0])):  #stlpec
        sucStlpca=0
        for i in range(len(A)): #riadok
            sucStlpca+=A[i][p]
        
        if p==0:
            maxSucStlpca=sucStlpca
        if sucStlpca>maxSucStlpca:
            maxSucStlpca=sucStlpca
            index=p
    return index

#print(indexMaxStlpca(matica))


def rovnakySucStlpcov(A):
    for p in range(len(A[0])):  #stlpec
        sucOverovaci=0
        for i in range(len(A)): #riadok
            sucOverovaci+=A[i][p]
        
        for pp in range(len(A[0])):
            suc=0
            for ii in range(len(A)):
                suc+=A[ii][pp]
            
            if suc==sucOverovaci and pp!=p:
                return True
    return False

#print(rovnakySucStlpcov(matica1))


#rekurzia
def returnRozZnaky(ret, t2):
    if len(ret)==0:
        return t2
    else:
        k=ret[0]
        ret=ret.replace(ret[0],'')
        t2.append(k)
        return returnRozZnaky(ret,t2)
    
#print(returnRozZnaky('skuska', []))



def returnRozZnaky1(ret):
    if len(ret)==0:
        return []
    else:
        return [ret[0]] + returnRozZnaky1(ret.replace(ret[0],''))
    
#print(returnRozZnaky1('skuska'))



def o_3_od_spoluziaka(ret):
    if not ret:
        return []
    elif ret[0] in ret[1:]:
        return o_3_od_spoluziaka(ret[1:])
    else:
        return [ret[0]] + o_3_od_spoluziaka(ret[1:])
    
def isPalindrom(ret):
    if len(ret)==0 or len(ret)==1:
        return True
    else:
        if ret[0]==ret[len(ret)-1]:
            return isPalindrom(ret[1:len(ret)-1])
        else:
            return False
        
print(isPalindrom('abba'))