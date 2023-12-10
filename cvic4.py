"""""
import turtle

#t = turtle.Turtle()

def testParity(n):
    if n%2==0:
        return True
    else: 
        return False
    
def minDvoch(n1,n2, n3):
    if n1<n2 and n1<n3:
        return n1
    elif n2<n3 and n2<n1:
        return n2
    elif n3<n2 and n3<n1:
        return n3
    

def menu():
    n=input('write your symbol: ')

    if n=='s':
        for i in range(4):
            t.forward(100)
            t.left(90)

    if n=='t':
        for i in range(3):
            t.left(120)
            t.forward(100)
    turtle.done()


def pocRovna(a,b,c):
     if a==b and a==c:
         return 3
     elif a==b or a==c or b==c:
         return 2
     else:
         return 0
     



def del5():
    suc=0
    for i in range(n):
        if a[i]%5==0:
            suc=suc+1
    return suc

a=[]
n=int(input())
for i in range(n):
    a.append(int(input('zadaj cislo: ')))

succ=0
for i in range(n):
    b=int(input('zadaj ', i+1, '. cislo: '))
    if b%5==0:
        succ=succ+1

print(succ)

print(del5())



n=int(input('zadaj kolko chces cisel: '))
succ=0
for i in range(n):
    b=int(input('zadaj cislo: '))
    succ=succ+b

print(succ)

n=int(input('zadaj kolko chces cisel: '))
b=int(input('zadaj cislo: '))
min=b
for i in range(n-1):
    b=int(input('zadaj cislo: '))
    if b<min:
        min=b

print(min)
"""""

arr=[]
n=int(input('zadaj pocet cisel: '))
for i in range(n):
    arr.append(int(input('zadaj cislo: ')))

def predMax():
    predMax=0
    maxx=0
    arr[0]=maxx
    for i in range(1,n):
        if arr[i]>maxx:
            predMax=maxx
            maxx=arr[i]
    return predMax

print(predMax())


def delitelnost(c,d):
    for i in range(1,c+1):
        if c%(i)==0:
            print(i)
    if c%d==0:
        return True
    else:
        return False
    
#print(delitelnost(12,7))

def testPrvoCis(c):
    testPrvoCis=True
    for i in range(2,c):
        if c%i==0:
            testPrvoCis=False
    return testPrvoCis

print(testPrvoCis(2))

for i in range(51):
    if testPrvoCis(i)==True:
        print(i)

print()