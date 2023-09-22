def filtra_pares(t):
	w=t[0:1]
	x=t[1:2]
	y=t[2:3]
	z=t[3:]
	n=[w,x,y,z]
	lista2 = []
for valor in n:
    if valor % 2 == 0:
        lista2.append(valor)