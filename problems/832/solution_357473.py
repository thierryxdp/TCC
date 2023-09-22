def eh_quadrada(matriz):
    x=len(matriz)
	y=len(matriz[0])
    if x==1:
        return True
    if x == y:
        return True
    else:
        return False