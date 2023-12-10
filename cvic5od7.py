def move(f,t):
    print('Move disc from ', f, ' to ', t)

def hanoi(n,f,h,t):
    if n==0:
        pass
    else:
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)
        print('')

#hanoi(4,'A', 'B', 'C')


def isPal(s,n):  #8.
    if (len(s)%2==0 and len(s)-n==n and s[n-1]==s[len(s)-n]) or (len(s)%2==1 and s[n-1]==s[len(s)-n]):
        return True
    else:
        if s[n-1]==s[len(s)-n]:
            return isPal(s,n+1)
        else:
            return False
        
#print(isPal('anna',1))




def isPower(n,k):   #9.
    if n==1:
        return True
    elif n%k!=0:
        return False
    else:
        return isPower(n/k, k)
    
#print(isPower(80,3))


def gcd(m,o,k): #10.
    if k%m==0 and o%m==0:
        return m
    else:
        return gcd(m-1,o,k)
    
#print(gcd(30,30,40))


def toBin(n): #12.
    if n==0:
        return '0'
    else:
        return str(toBin(n//2))+str(n%2)
    
#print(toBin(31))


def centDef(sum, poc):
    print(sum,' ', poc)
    if sum==0 and poc==0:
        return True  
    else:
        if sum-0.5>=0:
            return centDef(sum-0.5,poc-1)
        elif sum-0.2>=0:
            return centDef(sum-0.2,poc-1)
        elif sum-0.1>=0:
            return centDef(sum-0.1,poc-1)
        elif sum-0.05>=0:
            return centDef(sum-0.05,poc-1)
        elif sum-0.02>=0:
            return centDef(sum-0.02,poc-1)
        elif sum-0.01>=0:
            return centDef(sum-0.01,poc-1)
        else:
            return False
        
#print(centDef(0.6,2))


def moze_vytvorit_sumu(sum_v_eurach, pocet_minci, dostupne_mince):
    # Základný prípad: Ak je suma 0, tak sme ju úspešne vytvorili.
    if sum_v_eurach == 0:
        return True
    # Ak už nemáme mince k dispozícii alebo suma je negatívna, nevieme ju vytvoriť.
    if sum_v_eurach < 0 or pocet_minci == 0:
        return False
    # Rekurzívne volanie pre každú mincu, pri ktorej urobíme výber alebo necháme mincu pre ďalší pokus.
    for minca in dostupne_mince:
        if moze_vytvorit_sumu(sum_v_eurach - minca, pocet_minci - 1, dostupne_mince):
            return True
    return False


dostupne_mince = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50]  # Dostupné mince

vysledok = moze_vytvorit_sumu(0.04, 2, dostupne_mince)
if vysledok:
    print("Môžete vytvoriť zadanú sumu.")
else:
    print("Nemôžete vytvoriť zadanú sumu.")



def hanoi_count(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Počet presunov pre n diskov je rovnaký ako 2 * počet presunov pre (n-1) diskov + 1.
    return 2 * hanoi_count(n - 1) + 1

# Príklad použitia:
n = 3  # Počet diskov
print('pocet presunov pre: ', n, ' diskov: ', hanoi_count(n))


print()