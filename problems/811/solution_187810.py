def colchao(medidas,H,L):
    '''entrada: os parametros de entrada sao uma lista com as dimenssões do colchão em cm, 
    ordenadas da menor para a maior, e dois inteiros H e L(altura e largura das portas (list,int,int)
    saida: retorna true caso o colchão passe pela porta ou false caso faça o contrario (bool)'''
	ListaDeAreas = [[medidas[0],medidas[1]],[medidas[1],medidas[2]],[medidas[0],medidas[2]]]
	Possibilidades =[]
	for area in ListaDeAreas:
		if area[0]*area[1] <= L*H:
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