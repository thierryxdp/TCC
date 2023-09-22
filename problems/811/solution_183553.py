def colchao(medidas,H,L):
    '''uma função que calcula se um colchão de dimensões A*B*C consegue passar por uma porta de altura H 
    e largura L. 
    tupla -> booleano'''
    medidas[1] or medidas[2] < H or L
    return True