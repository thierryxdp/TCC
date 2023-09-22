def eh_quadrada(matriz):
    '''
Função que  retorna o booleano True se a matriz é quadrada ou False caso o contrário.

list-->bool
    '''
 
    
    if [] == matriz:
        return True
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False