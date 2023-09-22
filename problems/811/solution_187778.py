def colchao(medidas,H,L):
    ListaDeAreas = [[medidas[0],medidas[1]],[medidas[1],medidas[2]],[medidas[0],medidas[2]]]
    Possibilidades=[area for area in ListadeAreas if area[0]*area[1]<=L*H
    O_Movel_cabe=0
    for dupla in Possibilidades:
                    if dupla[0]<=L and dupla [1]<=H:
                    O_Movel_cabe = 1
                    	return True
                    if dupla[0] <=H and dupla[1] <=L:
                    O_Movel_cabe = 1
                    	return True
    if O_Movel_Cabe==0:
                    return False