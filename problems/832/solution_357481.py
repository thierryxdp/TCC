def eh_quadrada(matriz):
    x=len(matriz)
    if x>0:
		y=len(matriz[0])
    else:
        y=0
    if x == y:
        return True
    elif x != y:
        return False
    else:
        return True