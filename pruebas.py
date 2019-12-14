#Ejercicio: añade a El Rey Boo en la posición 4 del siguiente array

losMasGuays = ["Mariablo", "Deisanda", "Luigi", "Yoshi", "Peach", "Toad", "Wario"]
losMasGuaysfinal = ["Mariablo", "Deisanda", "Luigi","Rey Boo", "Yoshi", "Peach", "Toad", "Wario"]


losMasGuays.append("Rey Boo")
#losMasGuays = ["Mariablo", "Deisanda", "Luigi", "Yoshi", "Peach", "Toad", "Wario", "Rey Boo"]

tamani = len(losMasGuays)
pos = 3

for i in range(tamani-1, pos, -1):
    aux = losMasGuays[i-1]
    losMasGuays[i-1] = losMasGuays[i]
    losMasGuays[i] = aux
    print(losMasGuays)




if losMasGuays == losMasGuaysfinal:
    print("   ---OLE TU!!---   ")
else:
    print("   ---Intentalo otra vez---   ")