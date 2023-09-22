def eh_quadrada(matriz):
    a=len(matriz)
    for n in matriz:
    	b=len(matriz[0])
    
    if a==0:
        return True
    if a==b:
        return True
    else:
        return False