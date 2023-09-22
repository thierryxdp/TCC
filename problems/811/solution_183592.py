def colchao(medidas,H,L):
    '''uma função que calcula se um colchão de dimensões A*B*C consegue passar por uma porta de altura H 
    e largura L. 
    tupla, int, int -> booleano'''
    if (medidas[1] < H) or (medidas[1] < L) or (medidas[2] < H) or (medidas[2] < L) == True
        return True
    else:
        return False