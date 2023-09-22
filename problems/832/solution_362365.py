def eh_quadrada(matriz):
    '''
Função que  retorna o booleano True se a matriz é quadrada ou False caso o contrário.

list-->bool
    '''
    linha= len(matriz)
    coluna= len(matriz[0])
    if matriz==[]:
        return True
    if linha==coluna:
        return True
    else:
        return False