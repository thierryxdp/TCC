def colchao(medidas):
    '''uma função que calcula se um colchão de dimensões A*B*C consegue passar por uma porta de altura H 
    e largura L. 
    tupla -> booleano'''
    if (medidas[1] <= H or L):
        return True
    else:
        return False