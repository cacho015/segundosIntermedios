from datetime import datetime, date, time, timedelta

lista=[]
for x in range(0,60):

    #para la hora 10:00:00
    hora1 = datetime.combine(date.today(), time(10, 00, 00)) + timedelta(seconds=x)
    hstr1=hora1.time().strftime("%H:%M:%S")
    lista.append(hstr1)

for x in range(0,60):

    #para la hora 15:00:00
    hora2 = datetime.combine(date.today(), time(15, 00, 00)) + timedelta(seconds=x)
    hstr2=hora2.time().strftime("%H:%M:%S")
    lista.append(hstr2)

print(lista)