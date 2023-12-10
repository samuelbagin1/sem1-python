def ifLet(s,a):
    cont=0
    for i in range(len(s)):
        if s[i]==a:
            cont+=1
    return cont

#print(ifLet('banana', 'a'))


def isPal(s):
    if s==s[::-1]:
        return True
    else:
        return False
    
#print(isPal('oko'))


def ceasar(s,enc):
    ceasar=''
    for i in range(len(s)):
        if ord(s[i])>=65 and ord(s[i])<=90:
            if ord(s[i])+enc>90:
                ceasar=ceasar+chr(ord(s[i])+enc-26)
            elif ord(s[i])+enc<65:
                ceasar=ceasar+chr(ord(s[i])+enc+26)
            else:
                ceasar=ceasar+chr(ord(s[i])+enc)
        if ord(s[i])>=97 and ord(s[i])<=122:
            if ord(s[i])+enc>122:
                ceasar=ceasar+chr(ord(s[i])+enc-26)
            elif ord(s[i])+enc<97:
                ceasar=ceasar+chr(ord(s[i])+enc+26)
            else:
                ceasar=ceasar+chr(ord(s[i])+enc)
    return ceasar

#print(ceasar('B', -3))


def isBlank(s):
    for letter in s:
            if letter==' ':
                return False
    
fin=open('text.txt')
for line in fin:
    word=line.strip()
    if len(word)>20:
        if isBlank(word)!=False:
            print(word)


fin=open('words.txt')
def hasNoE(s):
    for letter in s:
        if letter=='e' or letter=='E':
            return True
       
pocE=0
pocAbs=0
for line in fin:
    word=line.strip()
    pocAbs+=1
    if hasNoE(word)==True:
        #print(word)
        pocE+=1
#print('percentage of words with e: ', pocE/pocAbs*100, '%')


def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

def uses_all(word, required):
    return uses_only(required, word)


def isAbecedarian(word):
    for i in range(len(word)):
        if ord(word[i])<ord(word[i-1]) and i>=1:
            return False
    return True

print(isAbecedarian('abdc'))

print()