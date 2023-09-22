def eh_quadrada(matriz):
    '''Função que retorna se uma matriz é quadrada ou não,
    recebe como argumento uma matriz dada pelo usuário;
    list(list)-->Boolean'''
    if len(matriz)==0 or len(matriz)==len(matriz[0]):
        return True
    else:
        return False