import random
import time
import copy

#sachovnicu vytvaram cez overovanie pozicie pomocou rozmeru
#nasledne sa to pripisuje do stringu a cely string printnem na konci ulohy

#v ulohach kde sa hrac pohybuje po hracej ploche vyuzivam funkciu playerPath(), ktora zmapuje resp. vytvory maticu/list kde sa na n-tom indexe nachadza suradnica tej pozicie 
#tuto je matica/cesta pre hraca so sachovnicou velkou 9, index 0-31 su hracie policka a 32,33,34 je domcek
#[[0, 5], [1, 5], [2, 5], [3, 5], [3, 6], [3, 7], [3, 8], [4, 8], [5, 8], [5, 7], [5, 6], [5, 5], [6, 5], [7, 5], [8, 5], [8, 4], [8, 3], [7, 3], [6, 3], [5, 3], [5, 2], [5, 1], [5, 0], [4, 0], [3, 0], [3, 1], [3, 2], [3, 3], [2, 3], [1, 3], [0, 3], [0, 4], [1, 4], [2, 4], [3, 4]]

#ak sa hrac nenachadza na hracej ploche ma poziciu [-1,-1]
#playerA/B - cesta po ktorej ide hrac, playerA/Bfigurky - list s poziciami danych figuriek

#fungujem na tom ze overujem figurky v playerA/Bfigurky s cestou playerA/B, dosadzujem nahodne cisla a overujem ci padla 6 atd.

#vypisovanie neviem ci bude presne s nahodnymi cislami (zalezi ci sa pozicia dosadzuje alebo sa figurka pohybuje), kedze som celu dobu pracoval s tym ze som vypisal nahodne cisla a az na konci while-loopu po podmienkach som vypisal sachovnicu
#bolo to lahsie na overenie ci to dobre dosadzuje pozicie/cisla

#podmienky by mali byt aj prelozene do normalnej reci, dufam ze pri vsetkych =), a tak isto aj funkcie a dosadzovannie
#pracoval som s globalnymi premennymi pre hraca A a B cize, podmienky/overovanie je tam 2x, vsetko by malo byt vysvetlne pri hracovi A
#pri hracovi B je to iste len v bledo-modrom

def gensachovnicu(n):       #vygenerovanie sachovnice
    #print('  ', end='')
    string='  '
    for i in range(n):      #vypis od 0 po n-1 na x-ovej osi
        #print(i-10 if i>=10 else i, end=' ')
        string+=str(i-10 if i>=10 else i)+' '
    #print('')
    string+='\n'

    for i in range(n):              #ostatok sachovnice
        #print(i-10 if i>=10 else i, end=' ')
        string+=str(i-10 if i>=10 else i)+' '
        for p in range(n):
            
            #zistovanie kde sa bude nachadzat */D/x/medzera na zaklade vypocitanej pozicie
            if ((n//2-1==p or n//2+1==p) and (i<n//2 or i>n//2)) or ((n//2-1==i or n//2+1==i) and (p<n//2 or p>n//2)) or (n//2==i and (p==0 or p==n-1)) or (n//2==p and (i==n-1 or i==0)):      #podmienky na vypis *
                #print('* ', end='')
                string+='* '
            elif (p==n//2 and ((i>=1 and i<=n//2-1) or (i>=n//2+1 and i<=n-1))) or (i==n//2 and ((p>=1 and p<=n//2-1) or (p>=n//2+1 and p<=n-1))):      #podmienky na vypis D
                #print('D', end=' ')
                string+='D '
            elif i==n//2 and p==n//2:       #podmienky pre x
                #print('x', end=' ')
                string+='x '
            else:       #vsetko ostatne medzera/prazdny priestor
                #print(' ', end=' ')
                string+='  '
        #print('')
        string+='\n'    #preskocenie do noveho riadku
    return string   #vratenie sachovnice

def tlacsachovnicu(k):
    if k%2==1:
        print(gensachovnicu(k))

#tlacsachovnicu(9)       #1. vypis prvej ulohy


###############################################################################################################################
#2.

#funckiu som vyuzil aj v tretej ulohe
#zistenie cesty hraca
def playerPath(n, startPos):  #rozmer hracej plochy, startovacia pozicia hraca
    pocH=4*(n-3)+8      #pocet */pocet miest kde hrac moze stupit - 8*(rozmer-3)/2+8 - pocet hviezdiciek aka pocet hracich stupienkov
    playerPosition=startPos.copy()     #startovacia pozicia priradena do pomocneho pola
    playerMove=[]   #trasa/cesta
    pocDom=(n-3)//2  #pocet domcekov

    for i in range(pocH+pocDom):
        playerMove.append(playerPosition.copy())    #zapisanie predchadzajucej pozicie

        if i>=pocH-1:       #podmienky kedy sa moze pripisovat domcek
            if startPos[0]==0 and startPos[1]==n//2+1:      #pre hraca A so start poziciou startPozA
                playerPosition[0]+=1
            elif startPos[0]==n-1 and startPos[1]==n//2-1:      #pre hraca B so start poziciou startPozB
                playerPosition[0]-=1
        else:       #pocitanie cesty/trasy, vychadzam z toho ze ked sa nachadza na rohovych miestach tak sa pozicia pricituje alebo odcituje
            if (((playerMove[i][0]<n//2-1 and playerMove[i][0>=0]) or (playerMove[i][0]>n//2 and playerMove[i][0]<n-1)) and playerMove[i][1]==n//2+1) or (playerMove[i][0]>=n//2-1 and playerMove[i][0]<=n//2 and playerMove[i][1]==n-1):   #move down
                playerPosition[0]+=1
            elif (((playerMove[i][0]<=n-1 and playerMove[i][0]>n//2+1) or (playerMove[i][0]<=n//2-1 and playerMove[i][0]>0)) and playerMove[i][1]==n//2-1) or (playerMove[i][0]<=n//2+1 and playerMove[i][0]>=n//2 and playerMove[i][1]==0):    #move up
                playerPosition[0]-=1
            elif (((playerMove[i][1]<=n-1 and playerMove[i][1]>n//2+1) or (playerMove[i][1]<=n//2 and playerMove[i][1]>0)) and playerMove[i][0]==n//2+1) or (playerMove[i][1]<=n//2+1 and playerMove[i][1]>=n//2 and playerMove[i][0]==n-1):   #move left
                playerPosition[1]-=1
            else:   #move right
                playerPosition[1]+=1

    return playerMove       #vratenie trasy/cesty pre hraca



def hraPlayerOne(n, playerRoute):       #vygenerovanie sachovnice s hracom, modifikovana prva funkcia
    string='  '
    for i in range(n):      #vypis od 0 po n-1 na x-ovej osi
        string+=str(i-10 if i>=10 else i)+' '
    string+='\n'

    for i in range(n):              #ostatok sachovnice
        string+=str(i-10 if i>=10 else i)+' '
        for p in range(n):
            
            if playerRoute[poziciaA][0]==i and playerRoute[poziciaA][1]==p:     #ked hrac nachadza na aktualnej polohe napise A resp. priradi
                string+='A '
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



#2. hra jedneho hraca
#!!!!!!!pre spustenie hry pre jedneho hraca, odkomentuj rozmer, vymaz b=1 a aj podmienku 'and b==0'       !!!!!!!!!!!!!!!
rozmer=0
#rozmer=int(input('zadaj aku velku chces sachovnicu: '))
b=1
if rozmer%2==1 and b==0:     #ak je neparny rozmer hrame
    vitaz=False
    playerA=playerPath(rozmer, [0,rozmer//2+1])       #cesta/trasa pre hraca A
    poziciaA=0      #zaciatok na nultej pozicii

    while vitaz!=True:
        print('')
        print('')

        nahCislo=random.randint(1,6)    #vygenerovanie nahodneho cisla
        poziciaA+=nahCislo      #pricitanie nahodneho cisla k pozicii figurky
        print('nahodne cislo padlo: ', nahCislo)

        if poziciaA>4*(rozmer-3)+7+(rozmer-3)/2:    #ak pozcicia presahuje index domceka tak sa cislo odcita a vypise sa sachovnica
            poziciaA-=nahCislo
            print(hraPlayerOne(rozmer, playerA))
        elif poziciaA>=4*(rozmer-3)+8 and poziciaA<=4*(rozmer-3)+7+(rozmer-3)/2:    #ak sa hrac nachadza v domceku koniec hry
            vitaz=True
            print(hraPlayerOne(rozmer, playerA))
        else:
            print(hraPlayerOne(rozmer, playerA))

        #time.sleep(2)   #casovy delay"



########################################################################################################################################
#3.


def hraPlayerTwo(n, playerOne, playerTwo):       #vygenerovanie sachovnice s hracomA a hracomB, n - je rozmer sachovnice, modifikovana prva funkcia
    string='  '
    for i in range(n):      #vypis od 0 po n-1 na x-ovej osi
        string+=str(i-10 if i>=10 else i)+' '
    string+='\n'

    for i in range(n):              #ostatok sachovnice
        string+=str(i-10 if i>=10 else i)+' '
        for p in range(n):
            b=False

            for k in range(len(playerOne)):     #prejdenie hracovho arsenalu ci sa jeho figurky rovnaju pozicii
                if playerOne[k][0]==i and playerOne[k][1]==p:     #ked hrac nachadza na aktualnej polohe napise A resp. priradi
                    string+='A '
                    b=True
                elif playerTwo[k][0]==i and playerTwo[k][1]==p:       #ked hrac nachadza na aktualnej polohe napise B resp. priradi
                    string+='B '
                    b=True

            if b==False:
                if ((n//2-1==p or n//2+1==p) and (i<n//2 or i>n//2)) or ((n//2-1==i or n//2+1==i) and (p<n//2 or p>n//2)) or (n//2==i and (p==0 or p==n-1)) or (n//2==p and (i==n-1 or i==0)):      #podmienky na vypis *
                    string+='* '
                elif (p==n//2 and ((i>=1 and i<=n//2-1) or (i>=n//2+1 and i<=n-1))) or (i==n//2 and ((p>=1 and p<=n//2-1) or (p>=n//2+1 and p<=n-1))):      #podmienky na vypis D
                    string+='D '
                elif i==n//2 and p==n//2:       #podmienky pre x
                    string+='x '
                else:       #vsetko ostatne medzera/prazdny priestor
                    string+='  '

        string+='\n'    #preskocenie do noveho riadku
    return string   #vratenie sachovnice


def dosadenieFigurPri6(playerFigurky):     #funkcia na ooverenie pri dosadeni 6, funkcia vrati index najblizsej figurky v domceku
    for findMinusPos in playerFigurky:
        if findMinusPos==[-1,-1] and playerFigurky.index(findMinusPos)>0:   #najde prvu poziciu s [-1,-1] ale musi byt index vacsi ako 0
            return playerFigurky.index(findMinusPos)
        
def cistaStartPoz(playerFigurky, startPoz): #overenie ci je cista startovacia pozicia
    for poz in playerFigurky:
        if poz==startPoz:       #ak sa pozicia rovna startovaciej pozicii funckia vrati False tz. ze nieje cista
            return False
    return True

def ifVsetkyMinus(playerFigurky):   #funkcia na overenie ci su vsetky minusove pozicie resp. ci ani jedna neni v hre
    for poz in playerFigurky:
        if poz!=[-1,-1]:    #ak sa najde prva neminusova pozicia funckia vrati False tz. ze nie su vsetky v domceku
            return False
    return True

def findNajblizsie(playerFigurky, playerRoute, n):  #funckia na najdenie najvzdialenejsej figurky resp, najblizsej k domceku
    maxIndex=0
    pocH=4*(n-3)+8 #pocet hracich miest
    for poz in playerFigurky:
        if poz!=[-1,-1]:    #pokial sa pozicia nerovna minusovej pozicii tak mozme overit dalej
            if playerRoute.index(poz)>maxIndex and playerRoute.index(poz)<pocH: #hladanie max indexu - index musi byt mensi ako pozicie domceku ktore sa v ceste hraca nachadzaju na posledny miestach s najvacsim indexom
                maxIndex=playerRoute.index(poz)
    return maxIndex     #vratenie najvacsieho indexu

def ifVsetkyVhre(playerFigurky):    #overenie ci su vsetky figurky v hre
    for poz in playerFigurky:
        if poz==[-1,-1]:    #ak sa jedna z prvych figurok rovna minusovej pozicii funkcia vrati False tz. ze nie su vsetky v hre
            return False
    return True
    
def ifPlaceFull(playerFigurky, nahCis, playerRoute):    #funckia na overenie, ked dosadim figurku ci je dane policko zabrate inou
    for poz in playerFigurky:       #obehne for-loopom figurky a ak sa pozicia rovna pozicii s nahodnym cislom funkcia vrati True a ak nenajdeme taku pozciu vrati False
        if playerRoute[nahCis]==poz:    
            return True
    return False

def ifVitaz(playerFigurky, playerRoute):    #overenie ci su vsetky figurky v domceku
    for poz in playerFigurky:
        if poz==[-1,-1]:    #ak sa jed a pozicia rovna minusovej vrati False a ak jeden index je mensi ako index domceku zas vrati False
            return False
        elif playerRoute.index(poz)<=4*(rozmer-3)+7:
            return False
    return True


def vyhodenieFigurky(playerFigurky1, playerFigurky2):       #ked figurka1 vstupy na policko figurky 2 tak potom sa figurka 2 vrati domov, funkcia vracia poziciu figurky2
    for poz in range(len(playerFigurky1)):
        for pozp in range(len(playerFigurky2)):
            if playerFigurky1[poz]==playerFigurky2[pozp]:
                return pozp
    return -1 #pre overennie

"""
if vyhodenieFigurky(playerAfigurky, playerBfigurky)>=0:
    playerBfigurky[vyhodenieFigurky(playerAfigurky, playerBfigurky)]=[-1,-1]        tato funkcia vykonava poslanie figurky do domceka
if vyhodenieFigurky(playerBfigurky, playerAfigurky)>=0:
    playerAfigurky[vyhodenieFigurky(playerBfigurky, playerAfigurky)]=[-1,-1]

"""

def printNahSach(hrac, nahC):   #vytlaci sachovnicu s vygenerovanym cislom pre daneho hraca
    print('nahodne cislo hraca ', hrac, ': ', nahC)
    print(hraPlayerTwo(rozmer, playerAfigurky, playerBfigurky))

def ifPlacePlusNahCisloFull(playerFigurky, nahC, playerRoute):  #funkcia na overenie ci mozme posunut dalej figurku, resp. ked chcem vstupit do domceka tak ci je dane miesto volne
    for poz in playerFigurky:
        if playerRoute[findNajblizsie(playerFigurky, playerRoute, rozmer)+nahC]==poz:
            return True
    return False

def atLeastOnInGame(playerFigurky, playerRoute):
    for poz in playerFigurky:
        if poz!=[-1,-1]:
            if playerRoute.index(poz)<=4*(rozmer-3)+7:
                return True
    return False







#3. hra dvoch hracov
rozmer=int(input('zadaj aku velku chces sachovnicu: '))
if rozmer%2==1:     #ak je neparny rozmer hrame
    vitaz=False

    startPozA=[0,rozmer//2+1]       #vypocet startovacej pozicie pre hraca A a hraca B
    startPozB=[rozmer-1, rozmer//2-1]


    playerA=playerPath(rozmer, startPozA)       #cesta/trasa pre hraca A
    playerB=playerPath(rozmer,startPozB)        ##cesta/trasa pre hraca B
    playerAfigurky=[]
    playerBfigurky=[]
    pocFiguriek=(rozmer-3)//2

    
    
    for pocetFigur in range(pocFiguriek):       #vytvorenie pozicii v domceku
        playerAfigurky.append([-1,-1])
        playerBfigurky.append([-1,-1])



    while vitaz!=True:
        print('')
        print('')

        nahCisloA=random.randint(1,6)    #vygenerovanie nahodneho cisla
        printNahSach('A', nahCisloA)
        nahCisloB=random.randint(1,6)    #vygenerovanie nahodneho cisla
        printNahSach('B', nahCisloB)



        dosadenieA=False        #premenne ak sa nepohneme v jednom kroku
        dosadenieB=False
        

        

        

        if nahCisloA!=6 and ifVsetkyMinus(playerAfigurky)==True:      #ak nepadne 6 a nemame ziadnu figurku na ploche, mame 3 pokusy pokial nehodime 6 (tu su iba 2 lebo prvy uz bol na zaciatku while loopu)
            for pokus in range(2):                                      #a zaroven ziadna figurka nemoze byt na ploche
                nahCisloA=random.randint(1,6)
                if nahCisloA==6:        #ak padne 6 dosadime figurku na plochu a hodime este raz, potom sa posunie
                    playerAfigurky[0]=startPozA     #dosadenie figurky
                    if vyhodenieFigurky(playerAfigurky, playerBfigurky)>=0:     #overenie ci figurka vyhodi nejaku figurku
                        playerBfigurky[vyhodenieFigurky(playerAfigurky, playerBfigurky)]=[-1,-1]    #vyhodenie figurky
                    printNahSach('A', nahCisloA)
                    nahCisloA=random.randint(1,6)       #ak padla 6 tak generujeme este raz
                    break
                else:
                    printNahSach('A', nahCisloA)
        elif nahCisloA==6 and ifVsetkyMinus(playerAfigurky)==True:    #ak padne 6 a nemame na ploche figurky, dosadime na start poziciu a hodime este raz
            playerAfigurky[0]=startPozA     #dosadenie figurky
            if vyhodenieFigurky(playerAfigurky, playerBfigurky)>=0:     #overenie ci figurka vyhodi figurku druheho hraca, ak je index vacsi ako -1 vyhodi, (-1 je ked neohrozuje)
                playerBfigurky[vyhodenieFigurky(playerAfigurky, playerBfigurky)]=[-1,-1]
            printNahSach('A', nahCisloA)
            nahCisloA=random.randint(1,6)       #generovanie noveho nahodneho cisla

        if nahCisloB!=6 and ifVsetkyMinus(playerBfigurky)==True:      #to iste co mal hrac A len pre hraca B
            for pokus in range(2):
                nahCisloB=random.randint(1,6)
                if nahCisloB==6:
                    playerBfigurky[0]=startPozB
                    if vyhodenieFigurky(playerBfigurky, playerAfigurky)>=0:
                        playerAfigurky[vyhodenieFigurky(playerBfigurky, playerAfigurky)]=[-1,-1]
                    printNahSach('B', nahCisloB)
                    nahCisloB=random.randint(1,6)
                    break
                else:
                    printNahSach('B', nahCisloB)
        elif nahCisloB==6 and ifVsetkyMinus(playerBfigurky)==True:
            playerBfigurky[0]=startPozB
            if vyhodenieFigurky(playerBfigurky, playerAfigurky)>=0:
                playerAfigurky[vyhodenieFigurky(playerBfigurky, playerAfigurky)]=[-1,-1]
            printNahSach('B', nahCisloB)
            nahCisloB=random.randint(1,6)
            print('nahodne cislo hraca B: ', nahCisloB)    ####################

        


        if nahCisloA==6 and sum(playerAfigurky[0])>0 and findNajblizsie(playerAfigurky, playerA, rozmer)+nahCisloA<=4*(rozmer-3)+7+(rozmer-3)//2 and ifPlacePlusNahCisloFull(playerAfigurky, nahCisloA, playerA)==False:       #ak padla 6 a zaroven je prva figurka v hre a zaroven pri dosadeni nahodneho cisla figurka nepresiahne maximalnu poziciu domceka
            if cistaStartPoz(playerAfigurky, startPozA) and ifVsetkyVhre(playerAfigurky)==False:        #ak je cista startovacia pozicia a nie su vsetky figurku v hre tak dosadime figurku
                playerAfigurky[dosadenieFigurPri6(playerAfigurky)]=startPozA        #dosadime prvu nehranu figurku do hry
                if vyhodenieFigurky(playerAfigurky, playerBfigurky)>=0:     #znova overenie ci vyhadzuje
                    playerBfigurky[vyhodenieFigurky(playerAfigurky, playerBfigurky)]=[-1,-1]
                printNahSach('A', nahCisloA)
                nahCisloA=random.randint(1,6)       #vygenerovanie noveho random cisla lebo sme mali 6
                if ifPlaceFull(playerAfigurky, nahCisloA, playerA)==False:      #overenie ked sme dosadili ci sa figurka moze posunut na dane miesto
                    playerAfigurky[playerAfigurky.index(startPozA)]=copy.deepcopy(playerA[nahCisloA])  #skopirovanie pozicie z cesty na figurku ktora je na start pozicii
                    if vyhodenieFigurky(playerAfigurky, playerBfigurky)>=0:     #overenie na vyhodenie
                        playerBfigurky[vyhodenieFigurky(playerAfigurky, playerBfigurky)]=[-1,-1]
                    printNahSach('A', nahCisloA)
                else:       #ak sa neda dosadit na dane miesto, posunieme figurku co je najdalej v hre
                    poziciaNaj=playerAfigurky.index(playerA[findNajblizsie(playerAfigurky, playerA, rozmer)])   #najdenie najvzdalenejsej pozicie figurky resp. nam to vrati index pozicie
                    playerAfigurky[poziciaNaj]=copy.deepcopy(playerA[findNajblizsie(playerAfigurky, playerA, rozmer)+nahCisloA])  #skopirovanie pozicie z cesty pri dosadeni nahodneho cisla
                    if vyhodenieFigurky(playerAfigurky, playerBfigurky)>=0:
                        playerBfigurky[vyhodenieFigurky(playerAfigurky, playerBfigurky)]=[-1,-1]
                    printNahSach('A', nahCisloA)
                dosadenieA=True     #kedze sme uz figurku dosadili a nahodne cislo moze byt od 1 po 6 tak sme zabezpecili aby sa pri dalsom ife neposunula
            elif ifPlacePlusNahCisloFull(playerAfigurky, nahCisloA, playerA)==False:   #ak sa neda dosadit posunieme figurku co je najdalej v hre
                poziciaNaj=playerAfigurky.index(playerA[findNajblizsie(playerAfigurky, playerA, rozmer)])   #najdenie najvzdalenejsej pozicie figurky resp. nam to vrati index pozicie
                playerAfigurky[poziciaNaj]=copy.deepcopy(playerA[findNajblizsie(playerAfigurky, playerA, rozmer)+nahCisloA])        #skopirovanie pozicie z cesty pri dosadeni nahodneho cisla
                if vyhodenieFigurky(playerAfigurky, playerBfigurky)>=0:     #znova overenie pri vyhodeni
                    playerBfigurky[vyhodenieFigurky(playerAfigurky, playerBfigurky)]=[-1,-1]
                printNahSach('A', nahCisloA)

        if findNajblizsie(playerAfigurky, playerA, rozmer)+nahCisloA>4*(rozmer-3)+7+(rozmer-3)//2 and nahCisloA==6 and sum(playerAfigurky[0])>0:       #ak pri dosadeni nahodneho cisla presahuje naj poziciu domceka a zaroven nam padla 6
            while nahCisloA==6:
                nahCisloA=random.randint(1,6)   #loopujeme dokedy nepadne insie ciso nez 6
                printNahSach('A', nahCisloA)

        

        
################################## to iste co pri hracovi A #########################################################
        if nahCisloB==6 and sum(playerBfigurky[0])>0 and findNajblizsie(playerBfigurky, playerB, rozmer)+nahCisloB<=4*(rozmer-3)+7+(rozmer-3)//2 and ifPlacePlusNahCisloFull(playerBfigurky, nahCisloB, playerB)==False:       #posunutie hraca B ak je alebo su na ploche figurky
            if cistaStartPoz(playerBfigurky, startPozB) and ifVsetkyVhre(playerBfigurky)==False:
                playerBfigurky[dosadenieFigurPri6(playerBfigurky)]=startPozB
                if vyhodenieFigurky(playerBfigurky, playerAfigurky)>=0:
                    playerAfigurky[vyhodenieFigurky(playerBfigurky, playerAfigurky)]=[-1,-1]
                printNahSach('B', nahCisloB)
                nahCisloB=random.randint(1,6)
                if ifPlaceFull(playerBfigurky, nahCisloB, playerB)==False:
                    playerBfigurky[playerBfigurky.index(startPozB)]=copy.deepcopy(playerB[nahCisloB])
                    if vyhodenieFigurky(playerBfigurky, playerAfigurky)>=0:
                        playerAfigurky[vyhodenieFigurky(playerBfigurky, playerAfigurky)]=[-1,-1]
                    printNahSach('B', nahCisloB)
                else:
                    poziciaNaj=playerBfigurky.index(playerB[findNajblizsie(playerBfigurky, playerB, rozmer)])
                    playerBfigurky[poziciaNaj]=copy.deepcopy(playerB[findNajblizsie(playerBfigurky, playerB, rozmer)+nahCisloB])
                    if vyhodenieFigurky(playerBfigurky, playerAfigurky)>=0:
                        playerAfigurky[vyhodenieFigurky(playerBfigurky, playerAfigurky)]=[-1,-1]
                    printNahSach('B', nahCisloB)
                dosadenieB=True
            elif ifPlacePlusNahCisloFull(playerBfigurky, nahCisloB, playerB)==False:
                poziciaNaj=playerBfigurky.index(playerB[findNajblizsie(playerBfigurky, playerB, rozmer)])
                playerBfigurky[poziciaNaj]=copy.deepcopy(playerB[findNajblizsie(playerBfigurky, playerB, rozmer)+nahCisloB])
                if vyhodenieFigurky(playerBfigurky, playerAfigurky)>=0:
                    playerAfigurky[vyhodenieFigurky(playerBfigurky, playerAfigurky)]=[-1,-1]
                printNahSach('B', nahCisloB)

        if findNajblizsie(playerBfigurky, playerB, rozmer)+nahCisloB>4*(rozmer-3)+7+(rozmer-3)//2 and nahCisloB==6 and sum(playerBfigurky[0])>0:
            while nahCisloB==6:
                nahCisloB=random.randint(1,6)
                printNahSach('B', nahCisloB)    ###########################################################################
                


        #ak je nahodne cislo mensie ako 6, aspon prva figurka je v hre, najblizsia figurka pri dosadeni nahodneho cisla nepresahuje index domceka, este sme neposunuli figurku, ked dosadime nahodne cislo figurka nevstupi na policko kde je nasa druha figurka, aspon jedna figurka je na hracom policku okrem domceka
        if nahCisloA<6 and sum(playerAfigurky[0])>0 and findNajblizsie(playerAfigurky, playerA, rozmer)+nahCisloA<=4*(rozmer-3)+7+(rozmer-3)//2 and dosadenieA==False and ifPlacePlusNahCisloFull(playerAfigurky, nahCisloA, playerA)==False and atLeastOnInGame(playerAfigurky, playerA)==True:  #ak nam padlo cislo mensie ako 6 a zaroven sme figurku neposunuli a pri dosadeni nahodneho cisla figurka nepresahuje naj poziciu domceka
            poziciaNaj=playerAfigurky.index(playerA[findNajblizsie(playerAfigurky, playerA, rozmer)])   #najdenie indexu najvzdialenejsej figurky
            playerAfigurky[poziciaNaj]=copy.deepcopy(playerA[findNajblizsie(playerAfigurky, playerA, rozmer)+nahCisloA])    #zmena pozicie pri dosadeni nahodneho cisla
            if vyhodenieFigurky(playerAfigurky, playerBfigurky)>=0:     #overenie na vyhodenie figurky
                playerBfigurky[vyhodenieFigurky(playerAfigurky, playerBfigurky)]=[-1,-1]
            printNahSach('A', nahCisloA)
        ##########  to iste co v ife vyssie len pre hraca B
        if nahCisloB<6 and sum(playerBfigurky[0])>0 and findNajblizsie(playerBfigurky, playerB, rozmer)+nahCisloB<=4*(rozmer-3)+7+(rozmer-3)//2 and dosadenieB==False and ifPlacePlusNahCisloFull(playerBfigurky, nahCisloB, playerB)==False and atLeastOnInGame(playerBfigurky, playerB)==True:
            poziciaNaj=playerBfigurky.index(playerB[findNajblizsie(playerBfigurky, playerB, rozmer)])
            playerBfigurky[poziciaNaj]=copy.deepcopy(playerB[findNajblizsie(playerBfigurky, playerB, rozmer)+nahCisloB])
            if vyhodenieFigurky(playerBfigurky, playerAfigurky)>=0:
                playerAfigurky[vyhodenieFigurky(playerBfigurky, playerAfigurky)]=[-1,-1]
            printNahSach('B', nahCisloB)            ##################
            
        
        
        if ifVitaz(playerAfigurky, playerA) or ifVitaz(playerBfigurky, playerB):    #ak jeden hrac ma vsetky figurky v domceku hra sa skoncila
            vitaz=True


        
        #time.sleep(2)   #casovy delaygbfbfgbbvcb
        print()