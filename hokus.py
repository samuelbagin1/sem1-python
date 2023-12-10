import random
import time
import copy



def playerPath(n, startPos):  #rozmer hracej plochy, startovacia pozicia hraca
    pocH=4*(n-3)+8      #pocet */pocet miest kde hrac moze stupit - 8*(rozmer-3)/2+8 - pocet hviezdiciek aka pocet hracich stupienkov
    playerPosition=startPos.copy()     #startovacia pozicia priradena do pomocneho pola
    playerMove=[]   #trasa/cesta
    pocDom=(n-3)//2  #pocet domcekov

    for i in range(pocH+pocDom):
        playerMove.append(playerPosition.copy())    #zapisanie predchadzajucej pozicie

        if i>=pocH-1:       #podmienky kedy sa moze pripisovat domcek
            if startPos[0]==0 and startPos[1]==n//2+1:      #pre hraca A so start poziciou [0,5]
                playerPosition[0]+=1
            elif startPos[0]==n-1 and startPos[1]==n//2-1:      #pre hraca B so start poziciou [8,3]
                playerPosition[0]-=1
        else:       #pocitanie cesty/trasy
            if (((playerMove[i][0]<n//2-1 and playerMove[i][0>=0]) or (playerMove[i][0]>n//2 and playerMove[i][0]<n-1)) and playerMove[i][1]==n//2+1) or (playerMove[i][0]>=n//2-1 and playerMove[i][0]<=n//2 and playerMove[i][1]==n-1):   #move down
                playerPosition[0]+=1
            elif (((playerMove[i][0]<=n-1 and playerMove[i][0]>n//2+1) or (playerMove[i][0]<=n//2-1 and playerMove[i][0]>0)) and playerMove[i][1]==n//2-1) or (playerMove[i][0]<=n//2+1 and playerMove[i][0]>=n//2 and playerMove[i][1]==0):    #move up
                playerPosition[0]-=1
            elif (((playerMove[i][1]<=n-1 and playerMove[i][1]>n//2+1) or (playerMove[i][1]<=n//2 and playerMove[i][1]>0)) and playerMove[i][0]==n//2+1) or (playerMove[i][1]<=n//2+1 and playerMove[i][1]>=n//2 and playerMove[i][0]==n-1):   #move left
                playerPosition[1]-=1
            else:   #move right
                playerPosition[1]+=1

    return playerMove       #vratenie trasy/cesty pre hraca



def hraPlayerTwo(n, playerOne, playerTwo):       #vygenerovanie sachovnice s hracom, modifikovana prva funkcia
    t=True
    string='  '
    for i in range(n):      #vypis od 0 po n-1 na x-ovej osi
        string+=str(i-10 if i>=10 else i)+' '
    string+='\n'

    for i in range(n):              #ostatok sachovnice
        string+=str(i-10 if i>=10 else i)+' '
        for p in range(n):
            
            if t:       #potrebujeme vylucit bud A alebo * inac by pisalo A*
                for k in range(len(playerOne)):     #prejdenie hracovho arsenalu ci sa jeho figurky rovnaju pozicii
                    if playerOne[k][0]==i and playerOne[k][1]==p:     #ked hrac nachadza na aktualnej polohe napise A resp. priradi
                        string+='A '
                    elif playerTwo[k][0]==i and playerTwo[k][1]==p:       #ked hrac nachadza na aktualnej polohe napise B resp. priradi
                        string+='B '
            elif ((n//2-1==p or n//2+1==p) and (i<n//2 or i>n//2)) or ((n//2-1==i or n//2+1==i) and (p<n//2 or p>n//2)) or (n//2==i and (p==0 or p==n-1)) or (n//2==p and (i==n-1 or i==0)):      #podmienky na vypis *
                string+='* '
            elif (p==n//2 and ((i>=1 and i<=n//2-1) or (i>=n//2+1 and i<=n-1))) or (i==n//2 and ((p>=1 and p<=n//2-1) or (p>=n//2+1 and p<=n-1))):      #podmienky na vypis D
                string+='D '
            elif i==n//2 and p==n//2:       #podmienky pre x
                string+='x '
            else:       #vsetko ostatne medzera/prazdny priestor
                string+='  '

        string+='\n'    #preskocenie do noveho riadku
    return string   #vratenie sachovnice


def dosadenieFigurPri6(playerFigurky):     
    for findMinusPos in playerFigurky:
        if findMinusPos==[-1,-1] and playerAfigurky.index(findMinusPos)>0:
            return playerAfigurky.index(findMinusPos)
        
def cistaStartPoz(playerFigurky, startPoz):
    for poz in playerFigurky:
        if poz==startPoz:
            return False
    return True

def vsetkyFifurkyVhre(playerFigurky):
    for poz in playerFigurky:
        if poz==[-1,-1]:
            return False
    return True

def findNajblizsie(playerFigurky, playerRoute, n):
    maxIndex=playerRoute.index(playerFigurky[0])
    pocH=4*(n-3)+8 
    for poz in playerFigurky:
        if poz!=[-1,-1]:
            if playerRoute.index(poz)>maxIndex and playerRoute.index(poz)<pocH:
                maxIndex=playerRoute.index(poz)
    return maxIndex







#3. hra dvoch hracov
rozmer=int(input('zadaj aku velku chces sachovnicu: '))
if rozmer%2==1:     #ak je neparny rozmer hrame
    vitaz=False
    playerA=playerPath(rozmer, [0,5])       #cesta/trasa pre hraca A
    playerB=playerPath(rozmer,[8,3])        ##cesta/trasa pre hraca B
    playerAfigurky=[]
    playerBfigurky=[]
    pocFiguriek=(rozmer-3)//2
    
    for pocetFigur in range(pocFiguriek):
        playerAfigurky.append([-1,-1])
        playerBfigurky.append([-1,-1])



    while vitaz!=True:
        print('')
        print('')

        nahCisloA=random.randint(1,6)    #vygenerovanie nahodneho cisla
        nahCisloB=random.randint(1,6)    #vygenerovanie nahodneho cisla
        print('nahodne cislo hraca A: ', nahCisloA)
        print('nahodne cislo hraca B: ', nahCisloB)

        if nahCisloA!=6 and sum(playerAfigurky[0])<0:      #ak nepadne 6 a nemame ziadnu figurku na ploche, mame 3 pokusy pokial nehodime 6
            for pokus in range(3):
                nahCisloA=random.randint(1,6)
                if nahCisloA==6:        #ak padne 6 dosadime figurku na plochu a hodime este raz, potom sa posunie
                    playerAfigurky[0]=[0,5]
                    nahCisloA=random.randint(1,6)
                    break
        elif nahCisloA==6 and sum(playerAfigurky)<0:    #ak padne 6 a nemame na ploche figurky, dosadime na start poziciu a hodime este raz
            playerAfigurky[0]=[0,5]
            nahCisloA=random.randint(1,6)

        if nahCisloB!=6 and sum(playerBfigurky)<0:      #to iste len pre hraca B
            for pokus in range(3):
                nahCisloB=random.randint(1,6)
                if nahCisloB==6:
                    playerBfigurky[0]=[0,5]
                    nahCisloB=random.randint(1,6)
                    break
        elif nahCisloB==6 and sum(playerBfigurky)<0:
            playerBfigurky[0]=[0,5]
            nahCisloB=random.randint(1,6)       #####


        if nahCisloA==6 and sum(playerAfigurky[0])>0 and findNajblizsie(playerAfigurky, playerA, rozmer)+nahCisloA<=4*(rozmer-3)+8+(rozmer-3)//2:       #posunutie hraca A ak je alebo su na ploche figurky
            if cistaStartPoz(playerAfigurky, [0,5]):
                playerAfigurky[dosadenieFigurPri6(playerAfigurky)]==[0,5]
                nahCisloA=random.randint(1,6)
            else:
                poziciaNaj=playerAfigurky.index(playerA[findNajblizsie(playerAfigurky, playerA, rozmer)])
                playerAfigurky[poziciaNaj]=copy.deepcopy(playerA[findNajblizsie(playerAfigurky, playerA, rozmer)+nahCisloA])

        if findNajblizsie(playerAfigurky, playerA, rozmer)+nahCisloA>4*(rozmer-3)+8+(rozmer-3)//2 and nahCisloA==6:
            while nahCisloA==6:
                nahCisloA=random.randint(1,6)
                
        if nahCisloA<6 and sum(playerAfigurky[0])>0 and findNajblizsie(playerAfigurky, playerA, rozmer)+nahCisloA<=4*(rozmer-3)+8+(rozmer-3)//2:
            poziciaNaj=playerAfigurky.index(playerA[findNajblizsie(playerAfigurky, playerA, rozmer)])
            playerAfigurky[poziciaNaj]=copy.deepcopy(playerA[findNajblizsie(playerAfigurky, playerA, rozmer)+nahCisloA])

        

        if nahCisloB==6 and sum(playerBfigurky[0])>0 and findNajblizsie(playerBfigurky, playerB, rozmer)+nahCisloB<=4*(rozmer-3)+8+(rozmer-3)//2:       #posunutie hraca A ak je alebo su na ploche figurky
            if cistaStartPoz(playerBfigurky, [0,5]):
                playerBfigurky[dosadenieFigurPri6(playerBfigurky)]==[0,5]
                nahCisloB=random.randint(1,6)
            else:
                poziciaNaj=playerBfigurky.index(playerB[findNajblizsie(playerBfigurky, playerB, rozmer)])
                playerBfigurky[poziciaNaj]=copy.deepcopy(playerB[findNajblizsie(playerBfigurky, playerB, rozmer)+nahCisloB])

        if findNajblizsie(playerBfigurky, playerB, rozmer)+nahCisloB>4*(rozmer-3)+8+(rozmer-3)//2 and nahCisloB==6:
            while nahCisloB==6:
                nahCisloB=random.randint(1,6)
                
        if nahCisloB<6 and sum(playerBfigurky[0])>0 and findNajblizsie(playerBfigurky, playerB, rozmer)+nahCisloB<=4*(rozmer-3)+8+(rozmer-3)//2:
            poziciaNaj=playerBfigurky.index(playerB[findNajblizsie(playerBfigurky, playerB, rozmer)])
            playerBfigurky[poziciaNaj]=copy.deepcopy(playerB[findNajblizsie(playerBfigurky, playerB, rozmer)+nahCisloB])

            
        
            
        print(hraPlayerTwo(rozmer, playerAfigurky, playerBfigurky))
        time.sleep(2)   #casovy delay

print()