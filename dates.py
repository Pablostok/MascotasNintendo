# 8/6/1993      10:03:13

from datetime import datetime

# hoy = datetime.date.today()
# print(hoy)
#
# t = datetime.time(10, 3, 13)
# print(t)
# print("")
# print("Hora: ", t.hour)
# print("Minutos: ", t.minute)
# print("Segundos: ", t.second)

# x = datetime.datetime(1993, 6, 8, 10, 3, 13)

# print(x.strftime("%d %b %Y %H:%M:%S"))

arrayfechas = ['6/7/2020 10:30', "6/7/2020 14:30", "6/7/2020 17:00"]

formato = '%d/%m/%Y  %H:%M'

aux = datetime.strptime(arrayfechas[0], formato)

print(aux)

aux2 = datetime.strptime(arrayfechas[1], formato)

if aux > aux2:
    print("aux1 > aux2")
else:
    print("aux2 > aux1")