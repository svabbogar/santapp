# ures lista, amibe lehet majd pakolni
adatok = []
# f valtozoba nyitjuk meg a fajlt
f = open("gecaj.txt", "r")

# belepakoljuk a sorokat egy listaba
# minden sor egy string, ami utan uj sor van amit \n jelol
# tehát minden sor valami ilyesmi: "blabla\n"
for x in f:
  adatok.append(x)

# teszteljuk
print(adatok)

# keressuk meg pl az outdoor_temperature erteket

# keressuk a listaban hanyadik index alatt van az outdoor_temperature, es hozzaadunk egyet, hogy kovetkezo sort adja (deg_C...)
out_c = adatok.index('[outdoor_temperature]\n') + 1
# itt belerakjuk az index alatt levo erteket
# tehat az adott sor "string" formaba
out_c = adatok[out_c]
# keressuk a sorban hol az elso es masodik idezojel
# a find() metodus az indexet adja vissza
elso_idezojel = out_c.find("\"")
print(elso_idezojel)

masodik_i = out_c.find("\"", int(elso_idezojel+1))
print(masodik_i)
# vegul valtoztassuk float tipusura es rakjuk bele a valtozoba
# float = valos szam, vagyis tizedes tort
out_c = float(out_c[elso_idezojel+1:masodik_i])
print(out_c)
# itt mar az out_c valtozo egy tizedestort tipusu erteket tartalmaz


# hogy at tudd majd irni a sajat dolgaidat csinalok ide meg egy sablont
# a [dewpoint] alatti celsius es farenheit adatot nyerjuk ki egy valtozoba:

#sorok indexei
dewpoint_index = adatok.index('[dewpoint]\n')
dewpoint_index_C = dewpoint_index + 1
dewpoint_index_F = dewpoint_index + 2

#a sort belerakjuk a valtozoba
dewpoint_C = adatok[dewpoint_index_C]
dewpoint_F = adatok[dewpoint_index_F]

#keressuk a ket idezojel indexeit
dp_C_elso = dewpoint_C.find("\"")
dp_C_masodik = dewpoint_C.find("\"", dp_C_elso+1)

dp_F_elso = dewpoint_F.find("\"")
dp_F_masodik = dewpoint_F.find("\"", dp_F_elso+1)

#kiszeleteljuk az elso idezojel es a masodik idezojel kozotti reszt
dewpoint_C = dewpoint_C[dp_C_elso+1 : dp_C_masodik]
dewpoint_F = dewpoint_F[dp_F_elso+1 : dp_F_masodik]
#vegul float tipusuva tesszuk
dewpoint_C = float(dewpoint_C)
dewpoint_F = float(dewpoint_F)

print("dewpoint_C = {}".format(dewpoint_C))
print("dewpoint_F = {}".format(dewpoint_F))

# remelem atlathato
# sok szerencset hozza