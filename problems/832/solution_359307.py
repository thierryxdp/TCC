def eh_quadrada(matriz:list)->bool:
    '''retorna True se a matriz é quadrada ou vazia'''
    if len(matriz) == len(matriz[0]) or []:
        return True 
    else:
        return False