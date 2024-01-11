noveny = input("Kérem a gyógynövény nevét: ")
mennyiseg = int(input("Kérem a napi szükséges mennyiséget grammban: "))

osszesen = 100 // mennyiseg
print(f"A(z) {noveny} összesen {osszesen} napra elegendő")
if osszesen > 30: 
    print("Elegendő 30 napra egy dobozzal!")
else:
    print("Egy doboz sajnos nem elegendő a 30 napra!")











