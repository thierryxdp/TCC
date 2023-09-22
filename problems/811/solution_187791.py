def movel(lista,H,L):
	ListaDeAreas = [[lista[0],lista[1]],[lista[1],lista[2]],[lista[0],lista[2]]]
	Possibilidades =[]
	for area in ListaDeAreas:
		if area[0]*area[1] <= L*H:
			print(area)
			Possibilidades = Possibilidades + [area]
	O_Movel_Cabe = 0
	for dupla in Possibilidades:
		if dupla[0] <= L  and dupla[1]<= H:
			O_Movel_Cabe = 1
			return True
		if dupla[0] <= H and dupla[1] <= L:
			O_Movel_Cabe = 1
			return True
	if O_Movel_Cabe == 0:
		return False