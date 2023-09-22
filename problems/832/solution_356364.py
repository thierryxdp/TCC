def eh_quadrada (lista):
    '''Funcao que identifica se a matriz é quadrada.
    list->bool'''
    
    matriz = []
        
    
    if len(lista)==0 or len(lista[0])==len(lista):
        return True
    else:
        return False