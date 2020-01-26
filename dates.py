# 8/6/1993      10:03:13

import datetime

# hoy = datetime.date.today()
# print(hoy)
#
# t = datetime.time(10, 3, 13)
# print(t)
# print("")
# print("Hora: ", t.hour)
# print("Minutos: ", t.minute)
# print("Segundos: ", t.second)

x = datetime.datetime(1993, 6, 8, 10, 3, 13)

print(x.strftime("%d %b %Y %H:%M:%S"))