def eh_quadrada(matriz):
    none=[[]]
    if matriz==none:
        return True
    while len(matriz) > 0 and len(matriz[0]) > 0:
        if len(matriz)!=len(matriz[0]):
            return False
        else:                   
            return True