tarol = []
f = open("novenyek.txt", mode="r", encoding="UTF-8")

for szo in f: 
   szavak = szo.strip()
   tarol.append(szavak.lower())
for item in tarol:
   osszesen = len(tarol)
   print(item)
print(f"A gyógynövények száma: {osszesen}")

noveny = input("Kérem adjon meg egy nevet: ")
if noveny in tarol: 
   print("Szerepel a listában")
else: 
   print("Nem szerepel a listában")

maganhangzok = ["e","u","i","o","ö","ü","ó","ő","ú","ű","a","é","á","í"]
tarol2 = []
for item in tarol:
   if item [0] in maganhangzok:
        tarol2.append(item)
print(tarol2)


sorrend = sorted(tarol)
print(F"A rendezett lista:\n{sorrend}")