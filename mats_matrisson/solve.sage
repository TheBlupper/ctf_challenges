import struct

t = 19871028092746200562
d = 31143324851076722529189336451008729704379858672550168591113427758662436634577754645297821879587920477504644205342388
c = 2505012059114305215676710070948712689694988127376946853904378804219365586439603775933545874906865477558869980349977799844263386384888039947026300989062807975

# Svaret ligger i ZZ (heltal) men Sage vill bara arbeta
# över en kropp (i.e QQ rationella tal), förhoppningsvis
# är svaret fortfarande ett heltal
P.<e1,e2,e3> = QQ[]

polys = []

# Tracen (spåret) är summan av egenvärderna
polys.append(e1+e2+e3 - t)

e1, e2, e3 = [8*e**2 - 5*e + 16 for e in (e1, e2, e3)]

# Determinanten är produkten av egenvärdena
polys.append(e1*e2*e3 - d)

e1, e2, e3 = [6*e**2 + 20*e - 3 for e in (e1, e2, e3)]

# Vietes formler ger ett uttryck för rötterna av ett polynom
# utifrån koefficienterna, och egenvärderna är
# röqterna till det karakteristiska polynomet
polys.append(e1*e2+e1*e3+e2*e3 - c)

# Utan att gå in i matten så hittar det här lösningar till
# ekvationssystemet. Ordningen på egenvärderna är okänd
# så vi printar alla kombinationer.
for sol in P.ideal(polys).variety():
    flag = struct.pack('QQQ', *sol.values()).decode()
    if flag.startswith('SSM{') and flag.endswith('}'):
        print(flag)