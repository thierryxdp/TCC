def colchao(medidas,H,L):
    '''uma função que calcula se um colchão de dimensões A*B*C consegue passar por uma porta de altura H 
    e largura L. 
    tupla -> booleano'''
    if (medidas[2] or medidas[3] < H or L):
        return True
    else:
        return False