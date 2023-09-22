#Start your python function here
par = []
for valor in filtra_pares:
    if valor % 2 == 0:
        par.append(valor)

print(par)