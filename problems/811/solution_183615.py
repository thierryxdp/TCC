def colchao(medidas,H,L):
    '''uma função que calcula se um colchão de dimensões A*B*C consegue passar por uma porta de altura H 
    e largura L. 
    tupla, int, int -> booleano'''
    (medidas[1] and  medidas[2] > H and L)