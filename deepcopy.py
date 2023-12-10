import copy


t1=[1,2,3]
t2=[4,5,6]
t3=[t1,t2]


##odkomentujte nasledujuce dva riadky a spustite skript
#t3[0][0]=5
#print(t1)
##nasledne riadky opat zakomentujte


##odkomentujte nasledujucich 5 riadkov a spustite skript. Uvidite, ze prikaz t3[:] vytvori kopiu z t3 iba na "prvej urovni"
##t4=t3[:]
##a= t4[0] is t1
##print(a)
##t4[0][0]=5
##print(t1)
##po spusteni skriptu riadky opat zakomentujte 


##ak chceme vytvorit kopiu z t3 na "vsetkych urovniach", mozeme pouzit funkciu deepcopy z modulu copy
##odkomentujte riadok "import copy" na vrchu skriptu
##odkomentujte nasledujucich 5 riadkov a spustite skript.
t5=copy.deepcopy(t3)
a= t5[0] is t1
print(a)
t5[0][0]=5
print(t5)

print()