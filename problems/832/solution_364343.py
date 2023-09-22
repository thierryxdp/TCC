def eh_quadrada(matriz_verif):
    '''
    funcao que retorna se uma matriz e quadrada
    ou nao apos ser inserida na entrada
    list->bool
    '''
    if matriz_verif==[]:
        return True 
    elif len(matriz_verif)==len(matriz_verif[0]):
        return True
    else:
        return False