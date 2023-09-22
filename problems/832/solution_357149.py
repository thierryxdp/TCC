def eh_quadrada(matriz):
    """ Funcao bool que diz se matriz eh qaudrada ou nao"""
    matriz=[]
    
    if len(matriz)*len(matriz[0]):
        return True
    else:
        False
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            i=j