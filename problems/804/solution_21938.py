def filtra_pares(t):
	w=t[0:1]
	x=t[1:2]
	y=t[2:3]
	z=t[3:]
	lista1 = [w,x,y,z]
	lista2 = []
for valor in lista1:
    if valor % 2 == 0:
        lista2.append(valor)