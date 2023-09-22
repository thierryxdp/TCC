def eh_quadrada(matriz):
    x=len(matriz)
	y=len(matriz[0])
    if x==0:
        return True
    if x == y:
        return x
    else:
        return False