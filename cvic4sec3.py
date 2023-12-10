def pohybVeze(x1,y1,x2,y2):
    if x1==x2 or y1==y2:
        return True
    else:
        return False

print()
print('veza: ')
print(pohybVeze(3,3,3,7))
print(pohybVeze(3,3,4,7))


#pri parnom y ma parne x ciernu a neparne x bielu
#pri neparnom y ma parne x bielu a neparne ciernu
def surColor(x,y):
    if y%2==0:
        if x%2==0:
            surColor='black'
        else:
            surColor='white'
    else:
        if x%2==0:
            surColor='white'
        else:
            surColor='black'
    return surColor

def rovnakaFarba(x1,y1,x2,y2):
    if surColor(x1,y1)==surColor(x2,y2):
        return True
    else:
        return False

print()
print('farba') 
print(rovnakaFarba(4,2,3,7))
print(rovnakaFarba(4,2,7,6))

def pohybKrala(x1,y1,x2,y2):
    if (x1==x2) and (y1-y2==1 or y2-y1==1):
        return True
    elif (y1==y2) and (x1-x2==1 or x2-x1==1):
        return True
    else:
        return False
    
print()
print('kral: ')
print(pohybKrala(3,3,4,3)) 
print(pohybKrala(3,3,4,5))


def pohybStrelca(x1,y1,x2,y2):
    if abs(y1-y2)==abs(x1-x2):
        return True
    else:
        return False
    
print()
print('strelec: ')
print(pohybStrelca(3,3,1,5))
print(pohybStrelca(3,3,1,4))


def pohybDamy(x1,y1,x2,y2):
    if pohybVeze(x1,y1,x2,y2)==True or pohybStrelca(x1,y1,x2,y2)==True:
        return True
    else:
        return False

print()
print('dama: ')
print(pohybDamy(3,3,8,3))
print(pohybDamy(3,3,5,4))


def pohybJazdca(x1,y1,x2,y2):
    if abs(y1-y2)==2 and abs(x1-x2)==1:
        return True
    elif abs(x1-x2)==2 and abs(y1-y2)==1:
        return True
    else:
        return False
    
print(' ')
print('knight: ')
print(pohybJazdca(5,4,3,3))
print(pohybJazdca(5,4,6,5))

print()